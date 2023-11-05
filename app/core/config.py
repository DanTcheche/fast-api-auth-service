from functools import lru_cache
from typing import Optional, Dict, Any, Union, List

from pydantic import BaseSettings, PostgresDsn, validator, AnyHttpUrl


class Settings(BaseSettings):
    API_VERSION: str = "v1"
    API_STR: str = f"/api/{API_VERSION}/auth"
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str = "5432"
    DATABASE_URI: Optional[PostgresDsn] = None
    BACKEND_CORS_ORIGINS: Union[List[str], List[AnyHttpUrl]]

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        """
        The assemble_db_connection function is a Pydantic validator that constructs and
        returns the PostgreSQL database connection string as a PostgresDsn object
        if the connection string is not already present.
        It takes three arguments: cls, which is the class where the validator is defined;
        v, which is the input value to validate; and values, which is a dictionary of previously validated values.
        If v is a string, it returns it as is. Otherwise, it uses the PostgresDsn.build() function
        to construct the connection string from the POSTGRES_USER, POSTGRES_PASSWORD,
        DATABASE_HOSTNAME, POSTGRES_PORT, and POSTGRES_DB values found in the values dictionary.
        Finally, it returns the resulting connection string as a PostgresDsn object.
        """
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("DATABASE_HOSTNAME"),
            port=str(values.get("POSTGRES_PORT")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


@lru_cache()
def get_settings():
    return settings
