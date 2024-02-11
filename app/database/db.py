from sqlmodel import Session, SQLModel, create_engine

from app.core.config import get_settings

settings = get_settings()
DATABASE_URL = settings.DATABASE_URI
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
