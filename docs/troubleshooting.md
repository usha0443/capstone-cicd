Troubleshooting Guide:

Frontend page not opening:
Problem: Browser does not show the frontend page  
Reason: Port 80 is already used on the local machine  
Fix: Use port 8080 and open http://localhost:8080  

Backend not responding:
Problem: Backend health check fails  
Reason: Backend container is not running  
Fix: Restart Docker containers  

Database error:
Problem: Backend cannot connect to database  
Reason: Database container is not running or wrong values  
Fix: Check database container and environment file  

Containers not starting:
Problem: Docker containers stop immediately  
Reason: Port conflict or configuration issue  
Fix: Check container logs  

CI/CD pipeline failed:
Problem: GitHub Actions shows error  
Reason: Docker Hub login or test failure  
Fix: Check GitHub secrets and pipeline logs  
