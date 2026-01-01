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
# Spring Batch vs Python Batch Framework

## Comparison Table

| Criteria                | Spring Batch (Java)                                                                 | Python Batch (Custom Framework)                                                                 |
|--------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Throughput**           | High throughput; optimized for millions of records with chunking, partitioning, and parallel steps | Moderate throughput; Python’s GIL limits threading, though multiprocessing can help for CPU-bound tasks |
| **Scalability**          | Scales horizontally with partitioned steps, remote chunking, and integration with enterprise schedulers | Scales vertically (multi-core) with `multiprocessing`; distributed scaling requires external frameworks (Dask, Ray, Spark) |
| **Fault Tolerance**      | Built-in retry, skip, restart, transaction management, and checkpointing | Basic retry/skip logic possible; restartability must be custom-coded (e.g., JSON checkpoints) |
| **Integration**          | Deep integration with Spring ecosystem (Spring Boot, Spring Data, Spring Cloud) | Lightweight; integrates easily with Python libraries (pandas, NumPy, SQLAlchemy) but lacks enterprise connectors |
| **Ease of Development**  | Steeper learning curve; requires Java, Spring configuration, XML/annotations | Very easy to prototype; concise syntax, fewer lines of code, highly flexible |
| **Monitoring & Ops**     | Mature tooling: Spring Batch Admin, Actuator, dashboards, logs | Must build custom monitoring/logging; limited out-of-the-box visibility |
| **Community & Support**  | Large enterprise adoption, strong documentation, long-term support | Smaller community for batch frameworks; Python ecosystem strong but fragmented |
| **Best Use Cases**       | Enterprise ETL, financial transactions, large-scale data migration, nightly jobs | Data science preprocessing, smaller ETL jobs, ad-hoc automation, educational/demo projects |

---

## Benchmark Experiment Plan (Processing 1 Million CSV Rows)

### Objective
Compare performance of **Spring Batch** vs **Python Batch Framework** when processing a CSV file with **1,000,000 rows**.

### Dataset
- **Input file:** `input.csv` with 1,000,000 rows
- Columns: `id, name, email`
- Synthetic data generated using Python script or Java utility

### Experiment Setup
1. **Spring Batch Job**
   - Reader: `FlatFileItemReader` for CSV
   - Processor: simple cleansing (trim strings, validate ID as integer)
   - Writer: `FlatFileItemWriter` to output CSV
   - Chunk size: 500
   - Parallelism: partitioned step with 4 threads
   - Metrics: execution time, throughput (rows/sec), memory usage

2. **Python Batch Job**
   - Reader: `CSVItemReader`
   - Processor: `CleanseProcessor` (same logic as Spring Batch)
   - Writer: `CSVItemWriter`
   - Chunk size: 500
   - Parallelism: `ProcessPoolExecutor` with 4 workers
   - Metrics: execution time, throughput (rows/sec), memory usage

### Measurement
- **Execution Time:** total time to process 1M rows
- **Throughput:** rows processed per second
- **Resource Usage:** CPU and memory consumption
- **Error Handling:** number of skipped/retried records

### Expected Outcome
- **Spring Batch:** Faster throughput, lower memory footprint, better monitoring
- **Python Batch:** Easier to implement, flexible, but slower for very large datasets

### Reporting
- Collect metrics into a table:

| Framework     | Time (seconds) | Throughput (rows/sec) | Memory Usage (MB) | Skipped Records |
|---------------|----------------|------------------------|-------------------|-----------------|
| Spring Batch  | TBD            | TBD                    | TBD               | TBD             |
| Python Batch  | TBD            | TBD                    | TBD               | TBD             |

---

## Notes
- Use the same machine/environment for both experiments to ensure fairness.
- Run multiple trials (e.g., 3 runs each) and average results.
- Consider scaling Spring Batch horizontally (partitioned jobs) vs Python Batch with distributed frameworks (Dask/Ray) for extended comparison.
