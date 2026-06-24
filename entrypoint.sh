#!/bin/sh

echo "Waiting for PostgreSQL..."
export PGPASSWORD="$POSTGRES_PASSWORD"
while ! pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  sleep 1
done

echo "PostgreSQL is ready"

echo "Applying migrations..."
alembic upgrade head

echo "Starting application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000