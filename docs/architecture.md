Container Architecture:

Overview:
This project is a 2-tier web application deployed using Docker and Docker Compose.

Components:
- Frontend: Nginx serving static HTML
- Backend: Flask application
- Database: PostgreSQL

Architecture Flow:
User → Nginx Frontend → Flask Backend → PostgreSQL Database

Docker Networking:
All containers run on a custom Docker bridge network so they can communicate using container names.

Data Persistence:
PostgreSQL data is stored using Docker volumes to ensure data is not lost when containers restart.

Architecture Diagram:

[Project Structure](images/project-structure.png)
[Running Containers](images/docker-ps.png)

User (Browser)
      |
      v
Frontend (HTML + CSS + JS)
      |
      v
Backend API (Flask)
      |
      v
PostgreSQL Database

Containerized view:

Browser
  |
  v
Frontend Container (Docker)
  |
  v
Backend Container (Flask + Docker)
  |
  v
PostgreSQL Container

