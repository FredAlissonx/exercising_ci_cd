from __future__ import annotations

import csv
from pathlib import Path


def _read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_daily_sales_summary(orders_path: Path, customers_path: Path) -> list[dict]:
    orders = _read_csv(orders_path)
    customers = _read_csv(customers_path)

    customer_lookup = {
        row["customer_id"]: {
            "customer_id": int(row["customer_id"]),
            "full_name": row["full_name"],
            "country": row["country"],
        }
        for row in customers
    }

    summary: dict[int, dict] = {}

    for row in orders:
        customer_id = int(row["customer_id"])
        amount = float(row["amount"])

        customer_info = customer_lookup.get(str(customer_id))
        if customer_info is None:
            raise ValueError(f"Order references unknown customer_id={customer_id}")

        if customer_id not in summary:
            summary[customer_id] = {
                **customer_info,
                "order_count": 0,
                "total_amount": 0.0,
            }

        summary[customer_id]["order_count"] += 1
        summary[customer_id]["total_amount"] += amount

    return list(summary.values())
