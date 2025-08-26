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

## Project Structure
- **`chinook-compose.yaml`**: Configures Docker services, volumes, and networking for PostgreSQL.
- **`Chinook_PostgreSql.sql`**: SQL scripts for schema and data initialization.
- **`chinook_password.txt`**: Contains the database password, managed securely via Docker Secrets.

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
