from uuid import UUID

from pydantic import Field, EmailStr

from src.schemas.base.base_entity import BaseEntity


class UserBase(BaseEntity):

    id: UUID = Field()
    email: EmailStr = Field()
    password: str = Field()
    active: bool = Field()


class UserCreate(UserBase):
    email: EmailStr
    password: str
    re_password: str


class UserUpdate(UserBase):
    password: str
    re_password: str
