## KaziRestaurant: Restaurant Management System

This document outlines KaziRestaurant, a Django-based web application designed for managing a restaurant's orders, products, and user accounts. It utilizes PostgreSQL as its database and employs Docker for containerized deployment, encompassing a frontend, backend, and database service.

## Django-Vuejs

### Features

- User authentication and management system
- Comprehensive product and order management
- RESTful API powered by Django REST framework
- Streamlined deployment using Docker

### Prerequisites

To get started, you'll need the following:

- **Docker:** Download and install Docker from the official website: [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
- **Docker Compose:** Follow the installation guide for Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

### Project Structure

Here's a breakdown of the project's directory structure:

```
.
├── backend
│   ├── Dockerfile (Defines build instructions for the backend container)
│   ├── manage.py (Django management script)
│   ├── requirements.txt (List of required Python packages)
│   └── kazirestaurant (Django application code)
│       ├── __init__.py (Empty file to mark directory as a package)
│       ├── settings.py (Project configuration settings)
│       ├── urls.py (Defines URL patterns for the application)
│       └── wsgi.py (WSGI entry point for the Django application)
├── frontend (Frontend code for the web application)
│   ├── Dockerfile (Defines build instructions for the frontend container)
│   ├── kazirestaurant_vue (Contains the frontend)
│   
└── docker-compose.yml (Defines configuration for managing Docker containers)
```

### Setup

Follow these steps to set up your development environment:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kazisohrabuddintitu/kazirestaurant.git
   cd kazirestaurant
   ```


2. **Create `.env` File:**

   - Create a file named `.env` in the project's root directory.
   - Add the following environment variables to the `.env` file, replacing placeholders with your database credentials:

   ```
   DATABASE_NAME=postgres
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

3. **Build and Run Docker Containers:**

   ```bash
   docker-compose build
   docker-compose up
   ```

   This command will build separate Docker images for the frontend, backend, and database services, and then start the corresponding containers.

   **Explanation:**

   - `docker-compose`: This command is used to manage Docker Compose projects.
   - `up`: This tells Docker Compose to start the services defined in `docker-compose.yml`.
   - `--build`: This option instructs Docker Compose to rebuild the images for the services before starting them (useful if you've made changes to the Dockerfile).

4. **Access the Application:**

   - Backend (API): http://localhost:8000
   - Frontend: http://localhost:8080 (The exact port might vary depending on your configuration)

### Stopping the Containers

To stop the running Docker containers, use the following command:

```bash
docker-compose down
```

### Development

**Rebuilding Docker Containers:**

If you make changes to either the `Dockerfile` or `requirements.txt` files, you'll need to rebuild the Docker containers before the changes take effect:

```bash
docker-compose build
```

This README provides a comprehensive guide to setting up and developing the KaziRestaurant application. Feel free to explore the code and customize it to suit your specific restaurant management needs.
