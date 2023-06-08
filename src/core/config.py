from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn, validator
from typing import Any, Dict, Optional


class Settings(BaseSettings):
    APP_NAME = "Auth Service"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    DATABASE_HOSTNAME: str
    ENVIRONMENT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()
APP_CONFIGS = {"title": settings.APP_NAME}
if settings.ENVIRONMENT != "local":
    APP_CONFIGS["openapi_url"] = None


@lru_cache()
def get_settings():
    return settings

