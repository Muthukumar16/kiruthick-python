# Python Batch Framework (Spring Batch Equivalent)

## Overview
This project provides a **Python-based batch processing framework** inspired by **Spring Batch**.  
It supports:
- Chunk-oriented processing (read → process → write)
- Restartability with checkpoints
- Retry and skip policies
- Step composition (multiple steps per job)
- Basic metrics (read, processed, written, skipped, failed)

---

## Features
- **ItemReader / ItemProcessor / ItemWriter** abstractions
- **CSV reader/writer** implementations
- **Checkpoint store** using JSON for restartability
- **SkipPolicy** for retry/skip handling
- **Job & Step execution** with metrics summary

---

## Project Structure
- batch_framework.py   # Core framework implementation
- input.csv             # Sample input file
- output.csv            # Generated output file
- customer_import_job_state.json  # Checkpoint state file

---

## Sample Input (input.csv)
```csv
id,name,email
1, Alice Johnson, alice.johnson@example.com
2, Bob Smith, bob.smith@example.com
3, Charlie Brown, charlie.brown@example.com
4, Diana Prince, diana.prince@example.com
5, Ethan Hunt, ethan.hunt@example.com
```

#### Example Usage
```batch
python batch_framework.py
```

#### Output
###### output.csv will contain cleansed records.

- customer_import_job_state.json will store checkpoint offsets.
- Console will display job summary:
```commandline
Job completed.
Step 1: read=5, processed=5, written=5, skipped=0, failed=0
```
