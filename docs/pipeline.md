CI/CD Pipeline Flow:

Trigger:
The pipeline is triggered whenever code is pushed to the main branch.

CI Stages:
1. Checkout source code from GitHub
2. Build Docker image for backend
3. Run unit tests inside Docker container
4. Scan Docker image using Trivy
5. Push Docker image to Docker Hub

CD Stages:
1. Staging server pulls latest Docker image
2. Old containers are stopped
3. New containers are started
4. Database migrations are executed
5. Application health is verified

Tools Used:
- GitHub Actions
- Docker
- Trivy
- Docker Hub

CI/CD Pipeline Proof:

[GitHub Actions Success](images/github-actions-success.png)
[Pipeline Logs](images/pipeline-logs.png)
[Docker Hub Image](images/dockerhub-image.png)
