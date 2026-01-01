# batch_framework.py
import csv
import json
import os
from typing import Iterable, Callable, Any, List, Optional

# -----------------------------
# Infrastructure: State & Utils
# -----------------------------
class CheckpointStore:
    def __init__(self, path: str = "state.json"):
        self.path = path
        self._state = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._state, f, indent=2)

    def get(self, key: str, default=None):
        return self._state.get(key, default)

    def set(self, key: str, value: Any):
        self._state[key] = value
        self.save()


# -----------------------------
# Contracts: Reader/Processor/Writer
# -----------------------------
class ItemReader:
    def open(self, checkpoint: Optional[Any] = None):
        pass

    def read(self) -> Optional[Any]:
        """Return next item or None when EOF."""
        return None

    def close(self):
        pass

    def checkpoint(self) -> Any:
        """Return a checkpoint token (e.g., offset)."""
        return None


class ItemProcessor:
    def process(self, item: Any) -> Any:
        """Transform/validate item; may raise to trigger retry/skip."""
        return item


class ItemWriter:
    def open(self):
        pass

    def write(self, items: List[Any]):
        pass

    def close(self):
        pass


# -----------------------------
# Concrete Readers/Writers
# -----------------------------
class CSVItemReader(ItemReader):
    def __init__(self, path: str, has_header: bool = True):
        self.path = path
        self.has_header = has_header
        self._file = None
        self._reader = None
        self._index = 0
        self._header_skipped = False

    def open(self, checkpoint: Optional[int] = None):
        self._file = open(self.path, "r", encoding="utf-8", newline="")
        self._reader = csv.reader(self._file)
        self._index = checkpoint or 0
        # Fast-forward to checkpoint
        for _ in range(self._index):
            try:
                next(self._reader)
            except StopIteration:
                break
        if self.has_header and not self._header_skipped and self._index == 0:
            next(self._reader, None)
            self._header_skipped = True
            self._index += 1

    def read(self) -> Optional[List[str]]:
        try:
            row = next(self._reader)
            self._index += 1
            return row
        except StopIteration:
            return None

    def close(self):
        if self._file:
            self._file.close()

    def checkpoint(self) -> int:
        return self._index


class CSVItemWriter(ItemWriter):
    def __init__(self, path: str, header: Optional[List[str]] = None, append: bool = True):
        self.path = path
        self.header = header
        self.append = append
        self._file = None
        self._writer = None
        self._initialized = False

    def open(self):
        mode = "a" if self.append else "w"
        self._file = open(self.path, mode, encoding="utf-8", newline="")
        self._writer = csv.writer(self._file)
        if not self.append and self.header:
            self._writer.writerow(self.header)
            self._initialized = True
        elif self.append and self.header and (not os.path.exists(self.path) or os.path.getsize(self.path) == 0):
            self._writer.writerow(self.header)
            self._initialized = True

    def write(self, items: List[Any]):
        for item in items:
            # accept lists/tuples/dicts
            if isinstance(item, dict):
                self._writer.writerow(list(item.values()))
            elif isinstance(item, (list, tuple)):
                self._writer.writerow(item)
            else:
                self._writer.writerow([item])

    def close(self):
        if self._file:
            self._file.close()


# -----------------------------
# Step & Job
# -----------------------------
class SkipPolicy:
    def __init__(self, max_retries: int = 1, skip_on_exception_types: Optional[tuple] = None):
        self.max_retries = max_retries
        self.skip_on_exception_types = skip_on_exception_types or (ValueError,)

    def should_retry(self, exc: Exception, attempts: int) -> bool:
        return attempts < self.max_retries

    def should_skip(self, exc: Exception) -> bool:
        return isinstance(exc, self.skip_on_exception_types)


class StepExecution:
    def __init__(self):
        self.read_count = 0
        self.process_count = 0
        self.write_count = 0
        self.skip_count = 0
        self.fail_count = 0


class Step:
    def __init__(
        self,
        name: str,
        reader: ItemReader,
        processor: ItemProcessor,
        writer: ItemWriter,
        chunk_size: int = 100,
        skip_policy: Optional[SkipPolicy] = None,
        checkpoint_key: Optional[str] = None,
    ):
        self.name = name
        self.reader = reader
        self.processor = processor
        self.writer = writer
        self.chunk_size = chunk_size
        self.skip_policy = skip_policy or SkipPolicy(max_retries=1)
        self.checkpoint_key = checkpoint_key or f"{name}.checkpoint"

    def execute(self, store: CheckpointStore) -> StepExecution:
        exec = StepExecution()
        checkpoint = store.get(self.checkpoint_key, None)
        self.reader.open(checkpoint)
        self.writer.open()

        chunk = []
        try:
            while True:
                item = self.reader.read()
                if item is None:
                    # flush remaining chunk
                    if chunk:
                        self.writer.write(chunk)
                        exec.write_count += len(chunk)
                        chunk = []
                    break

                exec.read_count += 1

                attempts = 0
                while True:
                    try:
                        processed = self.processor.process(item)
                        exec.process_count += 1
                        chunk.append(processed)
                        # flush if chunk full
                        if len(chunk) >= self.chunk_size:
                            self.writer.write(chunk)
                            exec.write_count += len(chunk)
                            chunk = []
                        break
                    except Exception as e:
                        attempts += 1
                        if self.skip_policy.should_retry(e, attempts):
                            continue
                        if self.skip_policy.should_skip(e):
                            exec.skip_count += 1
                            break
                        exec.fail_count += 1
                        raise

                # update checkpoint per item processed
                store.set(self.checkpoint_key, self.reader.checkpoint())

            # final checkpoint
            store.set(self.checkpoint_key, self.reader.checkpoint())
        finally:
            self.reader.close()
            self.writer.close()

        return exec


class JobExecution:
    def __init__(self):
        self.step_executions = []

    def summary(self) -> str:
        lines = []
        for i, se in enumerate(self.step_executions, start=1):
            lines.append(
                f"Step {i}: read={se.read_count}, processed={se.process_count}, "
                f"written={se.write_count}, skipped={se.skip_count}, failed={se.fail_count}"
            )
        return "\n".join(lines)


class Job:
    def __init__(self, name: str, steps: List[Step], checkpoint_store: Optional[CheckpointStore] = None):
        self.name = name
        self.steps = steps
        self.store = checkpoint_store or CheckpointStore(path=f"{name}_state.json")

    def run(self) -> JobExecution:
        je = JobExecution()
        for step in self.steps:
            se = step.execute(self.store)
            je.step_executions.append(se)
        return je


# -----------------------------
# Example: CSV cleanse and export
# -----------------------------
class CleanseProcessor(ItemProcessor):
    def process(self, item: List[str]) -> List[str]:
        # Example validations/transformations:
        # - Ensure first column is int
        # - Trim whitespace on all columns
        cleaned = [col.strip() for col in item]
        cleaned[0] = str(int(cleaned[0]))  # may raise ValueError -> triggers retry/skip
        return cleaned


def main():
    # Step 1: Ingest and cleanse input.csv -> output.csv
    reader = CSVItemReader(path="input.csv", has_header=True)
    processor = CleanseProcessor()
    writer = CSVItemWriter(path="output.csv", header=["id", "name", "email"], append=True)

    step1 = Step(
        name="cleanse_and_export",
        reader=reader,
        processor=processor,
        writer=writer,
        chunk_size=50,
        skip_policy=SkipPolicy(max_retries=2, skip_on_exception_types=(ValueError,)),
        checkpoint_key="step1.offset",
    )

    job = Job(name="customer_import_job", steps=[step1])
    result = job.run()
    print("Job completed.")
    print(result.summary())


if __name__ == "__main__":
    main()
