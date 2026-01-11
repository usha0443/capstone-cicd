#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Starting deployment to STAGING environment..."

# Load staging environment variables
export $(grep -v '^#' ./env/.env.staging | xargs)

# Pull latest images from Docker Hub
echo "Pulling latest Docker images..."
docker pull emmadiusha/capstone-backend:latest

# Stop and remove old containers
echo "Stopping existing containers..."
docker compose down

# Start containers with latest images
echo "Starting new containers..."
docker compose up -d

# Wait for services to initialize
echo "Waiting for services to be ready..."
sleep 10

# Run database migration
echo "Running database migration..."
./scripts/migrate.sh

# Health check
echo "Running health check..."
./scripts/health-check.sh

echo "Staging deployment completed successfully!"
