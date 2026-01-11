Demo Walkthrough – CI/CD Capstone Project:

Demo Objective:
To demonstrate an end-to-end CI/CD pipeline that builds, tests, scans, and deploys a Dockerized web application to a staging environment.

Step 1: Show Project Structure
- Display the project folders:
  - backend
  - frontend
  - docker-compose.yml
  - scripts
  - .github/workflows
  - docs
- Explain that the project uses Docker and GitHub Actions.

Step 2: GitHub Actions Pipeline:
- Push code to the main branch.
- Open GitHub → Actions tab.
- Show the CI/CD pipeline running.
- Explain pipeline stages:
  - Build Docker image
  - Run unit tests
  - Scan image using Trivy
  - Push image to Docker Hub

Step 3: Docker Hub:
- Open Docker Hub account.
- Show the repository with the latest image tag.
- Explain that the image was pushed automatically by the pipeline.

Step 4: Staging Deployment:
- Run the deployment script:
```bash
./scripts/deploy-staging.sh

Demo images:

[Staging Deployment](images/deploy-success.png)
[Backend Health](images/backend-health.png)
[Frontend UI](images/frontend-ui.png)
