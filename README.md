CI/CD Enabled Capstone Project – Application Health Monitoring System:

Overview:
This repository contains a containerized web application with a fully automated CI/CD pipeline.
The solution demonstrates modern DevOps best practices by integrating application development, Docker containerization, automated testing, security scanning, and staged deployment.

Objective:
The primary objective of this project is to showcase how a production-ready CI/CD workflow can be implemented using Docker and GitHub Actions, ensuring reliable, secure, and repeatable deployments.

Business Context:

In enterprise environments, manual builds and deployments often lead to errors, inconsistency, and delays.
This project addresses those challenges by implementing a fully automated CI/CD pipeline that:

1.Ensures consistent builds.
2.Detects defects early through automated testing.
3.Enforces security through container scanning.
4.Deploys validated images to a staging environment

Application Summary:

The application is a Health Monitoring System designed to verify the availability of application services.
It exposes a health check API that confirms:
1.Backend service availability.
2.Database connectivity status.
The system is designed to be lightweight, observable, and suitable for integration into real-world deployment pipelines.

Application Services:
The solution consists of the following containerized services:
Frontend Service:
A static web interface served using Nginx
Backend Service:
A Flask application exposing REST APIs, including a /health endpoint
Database Service:
PostgreSQL database used to validate backend connectivity and persistence
Each service runs independently inside Docker containers.

Technology Stack:
1.Frontend: HTML, CSS, JavaScript, Nginx
2.Backend: Python, Flask
3.Database: PostgreSQL
4.Containerization: Docker, Docker Compose
5.CI/CD Automation: GitHub Actions
6.Security Scanning: Trivy
7.Container Registry: Docker Hub

Architecture Overview:

The application follows a simple, scalable architecture

User → Nginx Frontend → Flask Backend → PostgreSQL Database

All services communicate through an isolated Docker network, ensuring separation of concerns and improved security.
Database data is persisted using Docker volumes to ensure durability across container restarts.

Local Development Setup:

Clone the Repository

git clone <https://github.com/usha0443/capstone-cicd.git>
cd cicd-docker-project

Start Application Services:

docker compose up --build -d

Verify Running Containers:

docker ps

Access the Application:

Frontend:

http://localhost:8080


Backend Health Endpoint:

http://localhost:5000/health


A successful response confirms that the backend service is running correctly.

Staging Environment Deployment:

The staging environment simulates a pre-production setup and validates the application after CI/CD execution.

Run Deployment Script:

./scripts/deploy-staging.sh

Deployment Actions Performed:
1.Pulls latest Docker images from Docker Hub
2.Stops existing containers
3.Starts new containers
4.Runs database migrations
5.Performs health check validation
Successful execution confirms a healthy staging deployment.

CI/CD Pipeline Description:
The CI/CD pipeline is automatically triggered on code changes pushed to the main branch.

Pipeline Stages:

1.Docker image build
2.Backend unit test execution inside containers
3.Container security scanning using Trivy
4.Image tagging and push to Docker Hub
5.Deployment to staging environment
This pipeline ensures secure, repeatable, and reliable deployments.

Testing Strategy:
Backend unit tests are executed inside Docker containers to maintain environment consistency.
Example:

docker run --rm <backend-image> pytest

Successful test execution validates application stability before deployment.

Database Management:
The PostgreSQL database runs as a dedicated container with persistent storage.

Access Database Container:

docker exec -it postgres_db psql -U <db_user> -d <db_name>

Validate Data:

SELECT * FROM users;

Exit database shell:

\q

Environment Isolation:
The solution enforces strict separation between local and staging environments.
Each environment uses:
1.Independent containers
2.Separate networks
3.Dedicated database volumes
This approach aligns with enterprise deployment standards and prevents unintended data overlap.

Deployment Validation:

Deployment success is validated using:
1.Container status checks
2.Backend health endpoint verification

docker ps
curl http://localhost:5000/health

Successful responses confirm a healthy deployment.

Documentation & Evidence:
All documentation and screenshots are available in the docs/images, including:
1.Architecture description
2.CI/CD pipeline flow
3.Deployment runbook
4.Troubleshooting guide
5.Demo walkthrough
Screenshots are stored in docs/images.

Conclusion:
This project demonstrates a professional CI/CD implementation aligned with modern enterprise DevOps practices.
It highlights:
1.Automated build and deployment pipelines
2.Containerized application architecture
3.Security scanning and validation
4.Environment isolation and staged deployments
The solution is suitable for real-world CI/CD workflows and can be extended to production environments with minimal changes.

Demo Video:
Demo video with audio:

https://1drv.ms/v/c/a6967f9f0fcd0c98/IQDc7EWyCEp8Rrks8cVv5E0pAY5ZYz0-milLrttqv-SFrKI?e=u6Ho76