from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from app.models.base_class import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = Column(String, unique=True, nullable=False)
