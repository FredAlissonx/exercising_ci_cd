from faker import Faker
import pandas as pd


def generate_fake_customers(count=5):
    fake = Faker()
    records = []

    for customer_id in range(1, count + 1):
        records.append(
            {
                "customer_id": customer_id,
                "full_name": fake.name(),
                "email": fake.email(),
                "city": fake.city(),
                "country": fake.country(),
            }
        )

    return pd.DataFrame(records)


def main():
    customers = generate_fake_customers()
    print(customers.to_string(index=False))


if __name__ == "__main__":
    main()
