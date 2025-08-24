
from dataclasses import dataclass

@dataclass
class app_env_settings:
    POSTGRES_USER: str = "myuser"
    POSTGRES_PASSWORD: str = "mypassword"
    POSTGRES_HOST: str = "localhost"
    # POSTGRES_HOST: str = "chinook-postgres"
    POSTGRES_PORT: str = 5432
    POSTGRES_DB: str = "chinook"