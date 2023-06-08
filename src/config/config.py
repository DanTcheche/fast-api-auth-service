from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME = "Auth Service"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    DATABASE_HOSTNAME: str
    ENVIRONMENT: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()
APP_CONFIGS = {"title": settings.APP_NAME}
if settings.ENVIRONMENT != "local":
    APP_CONFIGS["openapi_url"] = None


@lru_cache()
def get_settings():
    return settings

