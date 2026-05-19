from __future__ import annotations

from pathlib import Path

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from scripts.transform import build_daily_sales_summary


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


@dag(
    dag_id="daily_sales_summary",
    schedule="@daily",
    start_date=days_ago(1),
    catchup=False,
    tags=["analytics", "exercise"],
)
def daily_sales_summary():
    @task
    def check_source_files() -> list[str]:
        required_files = [
            DATA_DIR / "orders.csv",
            DATA_DIR / "customers.csv",
        ]
        missing = [str(path) for path in required_files if not path.exists()]
        if missing:
            raise FileNotFoundError(f"Missing source files: {missing}")
        return [str(path) for path in required_files]

    @task
    def validate_run_date(logical_date: str = "{{ ds }}") -> str:
        if logical_date > "{{ macros.ds_add(ds, 1) }}":
            raise ValueError("Run date cannot be in the future")
        return logical_date

    @task
    def transform_sales_data(_: list[str]) -> list[dict]:
        return build_daily_sales_summary(
            orders_path=DATA_DIR / "orders.csv",
            customers_path=DATA_DIR / "customers.csv",
        )

    @task
    def build_daily_summary(records: list[dict], run_date: str) -> dict:
        total_revenue = sum(record["total_amount"] for record in records)
        total_orders = sum(record["order_count"] for record in records)
        return {
            "run_date": run_date,
            "customer_count": len(records),
            "total_orders": total_orders,
            "total_revenue": round(total_revenue, 2),
        }

    @task
    def notify_success(summary: dict) -> None:
        print(f"Daily sales summary ready: {summary}")

    source_files = check_source_files()
    run_date = validate_run_date()
    transformed = transform_sales_data(source_files)
    summary = build_daily_summary(transformed, run_date)
    notify_success(summary)


daily_sales_summary()
