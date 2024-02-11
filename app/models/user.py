import uuid

from sqlmodel import Field

from app.db.base_class import Base


class User(Base, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True)
