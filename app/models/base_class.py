import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, func
from sqlalchemy.orm import Mapped, declared_attr, registry

mapper_registry: registry = registry()


@mapper_registry.as_declarative_base()
class Base:
    __abstract__ = True

    id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False
    )
    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
