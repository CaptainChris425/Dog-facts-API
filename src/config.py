import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = os.getenv("PORT", 3500)
    WORKERS: int = os.getenv("WORKERS", 3)
    RELOAD: bool = os.getenv("RELOAD", True)
    DEBUG: bool = os.getenv("DEBUG", True)
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")
