from uuid import uuid4, UUID

from sqlalchemy import Boolean, String
from sqlmodel import Field

from src.database.base_class import Base


class User(Base, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False,)
    email = Field(String, unique=True, index=True)
    hashed_password = Field(String)
    active = Field(Boolean, default=True)
