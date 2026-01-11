#!/bin/bash

set -e

echo "Starting database migration..."

# Load staging environment variables
export $(grep -v '^#' ./env/.env.staging | xargs)

# Execute SQL migration inside PostgreSQL container
docker exec -i postgres_db psql -U $DB_USER -d $DB_NAME < database/init.sql

echo "Database migration completed successfully"
