# sales-report

A Python script that reads a sales CSV file and writes a total-per-category report.

## What it does
Reads `sales.csv`, adds up the amounts for each category, and saves the result in `report.csv`.

## How it works
It reads each row with `csv.DictReader`, collects the totals in a dictionary, and writes them with `csv.writer`.

## How to run
In a terminal, run: `python sales.py`

## Example
Input (`sales.csv`):
date,category,amount
2026-10-01,Food,25.5
2026-10-02,Transport,10
2026-10-03,Food,12.75
2026-10-04,Books,40

Output (`report.csv`):
category,total
Food,38.25
Transport,10.0
Books,40.0

## Notes
- If `sales.csv` is missing, a clear message is shown.
- If an amount is not a number, the script stops with a clear message.
