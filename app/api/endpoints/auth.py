from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies.get_db import SessionDependency
from app.core.config import get_settings
from app.core.security import create_access_token
from app.repositories import users_repository
from app.schemas.token_schema import Token
from app.services.users_service import UserService

router = APIRouter()
settings = get_settings()


@router.post("/login/")
def login_access_token(
    session: SessionDependency,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = UserService(session, users_repository).authenticate(
        email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return Token(
        access_token=create_access_token(user.id, settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
