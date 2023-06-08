from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine

from src.config.config import get_settings

settings = get_settings()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=settings.ENVIRONMENT == "local")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    try:
        with Session(engine) as session:
            yield session
    finally:
        session.close()
