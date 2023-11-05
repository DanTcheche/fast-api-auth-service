from sqlmodel import create_engine, SQLModel, Session

from app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_DB}@db:{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
