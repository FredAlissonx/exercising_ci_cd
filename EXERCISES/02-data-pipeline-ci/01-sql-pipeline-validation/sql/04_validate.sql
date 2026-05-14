DO $$
DECLARE
    raw_count INTEGER;
    cleaned_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO raw_count FROM raw_orders;
    SELECT COUNT(*) INTO cleaned_count FROM cleaned_orders;

    IF raw_count <> 3 THEN
        RAISE EXCEPTION 'Expected 3 raw orders, got %', raw_count;
    END IF;

    IF cleaned_count <> 2 THEN
        RAISE EXCEPTION 'Expected 2 cleaned orders, got %', cleaned_count;
    END IF;
END $$;
