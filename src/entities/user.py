from typing import Optional
from uuid import UUID

from pydantic import Field

from src.entities.base.base_entity import BaseEntity


class BranchCategory(BaseEntity):

    id: Optional[UUID] = Field()
    email: str = Field()
    password: Optional[dict] = Field()
