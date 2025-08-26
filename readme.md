# Chinook PostgreSQL Docker Setup

## Project Overview
The Chinook PostgreSQL Docker project is designed to quickly set up a PostgreSQL database instance using Docker and Docker Compose. This setup is based on the Chinook sample database, which provides a ready-to-use schema and data ideal for testing and learning SQL queries and database concepts. The project serves educational purposes and helps developers who need a quick, scalable database setup for practice or application prototyping.

## Prerequisites
Before you begin, ensure you have the following software installed:
- **Docker**: Follow the official [installation guide](https://docs.docker.com/get-docker/) for your operating system.
- **Docker Compose**: Ensure you have Docker Compose set up. You can install it by following this [guide](https://docs.docker.com/compose/install/).

## Installation and Setup
### Cloning the Repository
To start using the project, clone the repository from your VCS:
```bash
git clone https://your-repo-url
cd your-repo-name
```

### Secrets Setup
Create a file named `chinook_password.txt` in the root directory. This file should contain the password for your PostgreSQL user. This password is used during the database setup to secure access.

### Building and Running the Containers
To build the Docker containers and start the services defined in Docker Compose:
```bash
docker compose -f chinook-compose.yaml up -d --build
```
This command will download the PostgreSQL image, initialize the database with Chinook schema, and set up a persistent data volume.

## Usage
### Starting and Stopping Services
- **Start the services**: Run the build command from the previous section to start services when they are not running.
- **Stop the services** while removing data: Use the command below to stop all containers and remove all associated volumes:
  ```bash
  docker compose -f chinook-compose.yaml down -v
  ```

### Interacting with the Database
Once the database is up, you can connect to it using a Postgres client, such as `psql` or graphical tools like DBeaver, using the following credentials:
- **Host**: `localhost`
- **Port**: `5432`
- **Database Name**: `chinook_db`
- **User**: `myuser`
- **Password**: *(your secret from chinook_password.txt)*

### Resetting Data
If you need to re-initialize the database with fresh data (loss of all current data):
```bash
docker compose -f chinook-compose.yaml down -v
docker compose -f chinook-compose.yaml up -d --build
```

## Project Structure
- **`chinook-compose.yaml`**: Defines the Docker services, volumes, and networks used in the project for setting up the Postgres environment.
- **`Chinook_PostgreSql.sql`**: Includes SQL commands executed for creating tables, views, and importing sample data when the database is initialized.
- **`chinook_password.txt`**: A sensitive file that contains the database user's password, used by Docker secrets.

## Configuration
### Docker Compose Configuration (`chinook-compose.yaml`)
- **Services**: Contains:
  - *db*: PostgreSQL container configuration
- **Environment Variables**:
  - PostgreSQL credentials are configured using environment variables such as `POSTGRES_USER`.
- **Secrets**:
  - `postgres_password`: Managed securely using Docker secrets, which reads from `chinook_password.txt`.
- **Volumes**:
  - Persist data using the `postgres_data` volume to ensure data isn't lost between container startups.
- **Networks**:
  - Integrate into an existing `app-network` for communication between other microservices or app components.

## Troubleshooting
- **Docker Not Starting**: Confirm Docker is running, and you have permissions to execute Docker commands.
- **Database Connection Issues**: Ensure correct network configuration and that the `postgres_password` secret is correctly set.

## Contributing
Contributions are welcome! Please follow the contributing guidelines and ensure changes are accompanied by tests. Fork the repository, create a branch, make your changes, and open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
