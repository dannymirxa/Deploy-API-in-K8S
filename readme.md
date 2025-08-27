# Chinook PostgreSQL Docker Setup

## Project Overview
The Chinook PostgreSQL Docker project quickly sets up a PostgreSQL database instance using Docker and Docker Compose. It leverages the Chinook sample database, perfect for testing and learning SQL queries and database concepts. The project serves educational and prototyping purposes.

## Prerequisites
Ensure the following software is installed before proceeding:
- **Docker**: Follow the official [installation guide](https://docs.docker.com/get-docker/) for specifics to your OS.
- **Docker Compose**: Install following this [guide](https://docs.docker.com/compose/install/).

## Installation and Setup

### Cloning the Repository
Clone the project repository:
```bash
git clone https://your-repo-url
cd your-repo-name
```

### Install dependencies
Install fastapi, sqlalchemy and asyncpg or you can use the `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Folder structure:
```ascii
/mnt/c/Projects/Deploy-API-in-K8S
├── __init__.py                    # Initialization file for Python packages
├── .gitignore                     # Specifies files and directories to be ignored by Git
├── chinook_password.txt           # File containing the password for the Chinook database
├── Chinook_PostgreSql.sql         # SQL script to set up the Chinook database schema
├── chinook-compose.yaml           # Docker Compose configuration for Chinook services
├── database.py                    # Handles database connections and operations
├── fastapi-compose.yaml           # Docker Compose configuration for FastAPI services
├── fastapi-dockerfile             # Dockerfile for building FastAPI application containers
├── main.py                        # Entry point for the FastAPI application
├── readme.md                      # Documentation file with an overview of the project
├── requirements.txt               # Specifies required Python packages and dependencies
├── server.py                      # Server-related configurations and setup
├── settings.py                    # Configuration and environment settings for the application
├── models                         # Directory containing data models
│   ├── customer_model.py          # Data model for customer-related database operations
│   └── employee_model.py          # Data model for employee-related database operations
├── router                         # Directory containing API route definitions
│   ├── __init__.py                # Initialization file for the router package
│   ├── customer_router.py         # API routes for customer-related operations
│   └── employee_router.py         # API routes for employee-related operations
├── schemas                        # Schema definitions for request and response data
│   ├── customer_schema.py         # Schema for customer data validation and serialization
│   └── employee_schema.py         # Schema for employee data validation and serialization
└── tests                          # Directory containing tests
    ├── test_crud.py               # Unit tests for CRUD operations
    ├── test_db.py                 # Unit tests for database connections and operations
    └── methods_for_pytest         # Directory containing test utility methods
        ├── methods_for_crud.py    # Helper methods for CRUD tests
        └── methods_for_db.py      # Helper methods for database tests

```

### Secrets Setup
Create a `chinook_password.txt` in the root directory with your PostgreSQL password. This password is securely handled using Docker Secrets.

### Building and Running the Containers
Build and start the Docker services:
```bash
docker compose -f chinook-compose.yaml up -d --build
```
This command initializes a PostgreSQL 17 instance with Chinook database schema, utilizing a persistent data volume.

## Usage

### Starting and Stopping Services

- **Start Services**: Use the build command from the setup section.
- **Stop Services and Remove Data**: To stop containers and remove all volumes, execute:
  ```bash
  docker compose -f chinook-compose.yaml down -v
  ```

### Interacting with the Database
Connect to the database via clients like `psql` or DBeaver using:
- **Host**: `localhost`
- **Port**: `5435`
- **Database Name**: `chinook`
- **User**: `myuser`
- **Password**: *(your secret from chinook_password.txt)*

### Resetting Data
To re-initialize the database with fresh data:
```bash
docker compose -f chinook-compose.yaml down -v
docker compose -f chinook-compose.yaml up -d --build
```

## Configuration

### Docker Compose Configuration (`chinook-compose.yaml`)
- **Services**: Includes
  - *db*: Configures PostgreSQL container
- **Environment Variables**:
  - Uses environment variables like `POSTGRES_USER`.
- **Secrets**: 
  - `postgres_password` is managed securely.
- **Volumes**:
  - Utilizes `postgres_data` volume for data persistence.
- **Networks**:
  - Connects via `app-network` to other microservices for integration.

## Troubleshooting
- **Docker Issues**: Ensure Docker is running and accessible.
- **Database Connection Errors**: Verify network setup and `postgres_password` secret.

## Contributing
Your contributions are welcome! Follow our guidelines, test changes, fork our repo, make a branch, commit your work, and open a pull request.

## License
This project operates under the MIT License. See the [LICENSE](LICENSE) file for details.
