# This stops the container and removes the persistent data volume
docker compose -f chinook-compose.yaml down -v

# This rebuilds and starts the container, which will re-run the corrected SQL script
docker compose -f chinook-compose.yaml up -d --build