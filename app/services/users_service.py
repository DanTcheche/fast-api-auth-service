from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.repositories.users_repository import UserRepository
from app.schemas.user_schema import UserInDBBase


class UserService:
    def __init__(self, session: Session, repository: UserRepository):
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
