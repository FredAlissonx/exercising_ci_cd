# Exercise 2.1 - SQL Pipeline Validation

This exercise is intentionally small. The goal is to keep the focus on the CI workflow that validates SQL, not on setting up a local database.

## Context

- GitHub Actions will create a temporary PostgreSQL database for the job.
- No local database is required on your machine.
- The workflow should create the schema, load sample data, run a transformation, and validate the result.

## Files

- `sql/01_schema.sql` creates the tables.
- `sql/02_seed.sql` inserts sample rows.
- `sql/03_transform.sql` runs the transformation query.
- `sql/04_validate.sql` checks the expected output.
