CREATE TABLE IF NOT EXISTS raw_orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS cleaned_orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL
);
