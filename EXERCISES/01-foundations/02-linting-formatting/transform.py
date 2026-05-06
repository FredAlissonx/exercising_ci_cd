from faker import Faker
import pandas as pd


def generate_customer_snapshot(count: int = 5) -> pd.DataFrame:
    fake = Faker()
    rows = []

    for customer_id in range(1, count + 1):
        rows.append(
            {
                "customer_id": customer_id,
                "full_name": fake.name(),
                "email": fake.email(),
                "city": fake.city(),
                "country": fake.country(),
            }
        )

    return pd.DataFrame(rows)


def clean_customer_snapshot(customers: pd.DataFrame) -> pd.DataFrame:
    cleaned = customers.copy()
    cleaned["email"] = cleaned["email"].str.lower().str.strip()
    cleaned["full_name"] = cleaned["full_name"].str.title().str.strip()
    cleaned["city"] = cleaned["city"].str.title().str.strip()
    cleaned["country"] = cleaned["country"].str.title().str.strip()
    return cleaned.sort_values("customer_id").reset_index(drop=True)


def main() -> None:
    raw_customers = generate_customer_snapshot()
    curated_customers = clean_customer_snapshot(raw_customers)
    print(curated_customers.to_string(index=False))


if __name__ == "__main__":
    main()
