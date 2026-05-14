INSERT INTO cleaned_orders (order_id, customer_name, amount)
SELECT order_id, customer_name, amount
FROM raw_orders
WHERE amount >= 100
ON CONFLICT (order_id) DO UPDATE
SET customer_name = EXCLUDED.customer_name,
    amount = EXCLUDED.amount;
