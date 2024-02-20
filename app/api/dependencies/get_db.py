from typing import Annotated, Generator

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.core.config import get_settings
from app.db.db import engine

settings = get_settings()

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_db)]
TokenDependency = Annotated[str, Depends(reusable_oauth2)]
