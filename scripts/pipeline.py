"""End-to-end: load → clean → join → monthly report.

Run from the project folder:  uv run python scripts/pipeline.py
Writes output/report.csv (one row per region and month) and prints a summary.
"""

from pathlib import Path

import pandas as pd

CUSTOMERS = Path("data/raw/customers.csv")
ORDERS = Path("data/raw/orders.csv")
OUT = Path("output/report.csv")


def load_customers() -> pd.DataFrame:
    df = pd.read_csv(CUSTOMERS)
    assert df.shape[1] == 4, f"expected 4 customer columns, got {df.shape[1]}: {list(df.columns)}"
    return df


def load_orders() -> pd.DataFrame:
    df = pd.read_csv(ORDERS)
    expected = ["order_id", "customer_id", "order_date", "amount", "status"]
    assert list(df.columns) == expected, f"unexpected columns: {list(df.columns)}"
    return df


def clean(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.copy()
    df["amount"] = df["amount"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df[df["status"] == "paid"]


def monthly_report(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    merged = orders.merge(customers, on="customer_id", how="left")
    report = merged.groupby(["region", "month"])["amount"].agg(["count", "sum"]).reset_index()
    report = report.rename(columns={"count": "orders", "sum": "revenue"})
    report["revenue"] = report["Revenue"].round(2)
    return report


def summary_line(report: pd.DataFrame) -> str:
    total = report["revenue"].sum()
    return "Total paid revenue: " + total


def main() -> None:
    customers = load_customers()
    orders = clean(load_orders())
    report = monthly_report(orders, customers)
    OUT.parent.mkdir(exist_ok=True)
    report.to_csv(OUT, index=False)
    print(report.head(8))
    print(summary_line(report))


if __name__ == "__main__":
    main()
