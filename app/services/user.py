from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.models import User
from app.repositories.users_repository import user_repository


class UserService:
    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = user_repository.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
