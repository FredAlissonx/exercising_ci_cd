# Exercise 2.3 - Airflow DAG Validation

This exercise simulates a small analytics team that uses Airflow to build a
daily sales summary for an e-commerce business.

## Scenario

Every morning, the BI team expects an updated sales summary generated from two
raw inputs:

- `data/orders.csv`
- `data/customers.csv`

The Airflow DAG should:

1. Confirm the expected source files exist.
2. Validate that the run date is not in the future.
3. Transform raw orders into customer-level sales metrics.
4. Build a daily summary payload for downstream analytics use.
5. Finish with a success notification step.

The business logic is intentionally simple. The actual challenge is CI:
developers keep merging broken DAG changes, and production only fails after the
DAG is deployed.

## Your CI Goal

Design a workflow that fails on pull requests whenever the DAG cannot be
imported or parsed correctly.

Examples of failures your CI should catch:

- Python syntax errors in `dags/daily_sales_summary.py`
- Missing imports in the DAG file
- Missing imports in local modules used by the DAG
- Invalid DAG definitions or broken task wiring

You do not need to:

- run a full Airflow environment
- execute the pipeline end to end
- deploy anything

## Files Included

- `dags/daily_sales_summary.py`: Airflow DAG to validate
- `scripts/transform.py`: local transformation module imported by the DAG
- `data/orders.csv`: sample raw order data
- `data/customers.csv`: sample customer data
- `requirements.txt`: minimal dependencies for the exercise

## Suggested Validation Cases

Use these to test your workflow:

1. Healthy DAG: pipeline passes.
2. Syntax error in the DAG: pipeline fails.
3. Fake package import in the DAG: pipeline fails.
4. Syntax or import error in `scripts/transform.py`: pipeline fails.
5. Broken DAG object or task dependency definition: pipeline fails.
