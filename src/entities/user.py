from uuid import UUID

from pydantic import Field

from src.entities.base.base_entity import BaseEntity


class User(BaseEntity):

    id: UUID = Field()
    email: str = Field()
    password: str = Field()
    active: bool = Field()

