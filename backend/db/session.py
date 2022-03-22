from email.generator import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings
from typing import Generator


SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()