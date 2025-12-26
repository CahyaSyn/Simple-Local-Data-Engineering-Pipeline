# Local Data Engineering Pipeline (Medallion Architecture)

## Overview
This project implements an end-to-end **local data engineering pipeline**
using **Medallion Architecture (RAW → BRONZE → SILVER → GOLD)**.

The pipeline ingests raw transaction data, cleans and structures it,
applies business logic, and produces analytics-ready datasets.

## Architecture
<img width="718" height="1095" alt="Data Pipeline Medalion Architecture (1)" src="https://github.com/user-attachments/assets/a46b6e71-3c78-4e14-83e4-2ebe7e56b40e" />



## Tech Stack
- Python 3.10
- PostgreSQL 14
- SQLAlchemy
- Pandas

## Data Layers
### RAW
Stores raw data as-is for traceability.

### BRONZE
Cleans and enforces data types.

### SILVER
Applies business logic and computes metrics.

### GOLD
Aggregates data for analytics and reporting.

## How to Run
```bash
python etl/run_all.py
```
## Example Analytics
```commandline
SELECT * FROM gold.daily_revenue
```
