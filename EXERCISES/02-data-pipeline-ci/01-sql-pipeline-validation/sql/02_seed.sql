INSERT INTO raw_orders (order_id, customer_name, amount)
VALUES
    (1, 'Ada Lovelace', 120.50),
    (2, 'Grace Hopper', 210.00),
    (3, 'Katherine Johnson', 98.25)
ON CONFLICT (order_id) DO NOTHING;
