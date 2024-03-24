from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.repositories.users_repository import UsersRepository
from app.schemas.user_schema import UserCreate, UserInDBBase


class UsersService:
    def __init__(self, session: Session, repository: UsersRepository):
        self.session = session
        self.repository = repository

    def authenticate(self, email: str, password: str) -> UserInDBBase | None:
        user = self.repository.get_by_email(self.session, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return UserInDBBase.model_validate(user)

    def get_by_id(self, user_id: UUID) -> UserInDBBase | None:
        user = self.repository.get(self.session, user_id)
        if not user:
            return None
        return UserInDBBase.model_validate(user)

    def create_user(self, user: UserCreate) -> UserInDBBase:
        user = self.repository.create(self.session, user)
        return UserInDBBase.model_validate(user)
