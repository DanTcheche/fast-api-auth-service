from uuid import uuid4, UUID

from sqlalchemy import Boolean, Column, String
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False,)
    email = Field(String, unique=True, index=True)
    hashed_password = Field(String)
    active = Field(Boolean, default=True)
