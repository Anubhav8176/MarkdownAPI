from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Markdown API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    DATABASE_URL: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }

@lru_cache
def get_settings()->Settings:
    return Settings()

settings = get_settings()