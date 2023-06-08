from datetime import datetime
from typing import Optional

from src.schemas.base.base_entity import BaseEntity


class SNResponseBaseModel(BaseEntity):
    echo_request: dict = {}
    data: Optional[dict]
    errors: Optional[list[dict]]
    timestamp: datetime = datetime.now()
