from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings


Base = declarative_base()

db_url = settings.DATABASE_URL

# Engine connects the actual database to this project.
db_engine = create_engine(url = db_url)

# Creates a local session for each request.
SessionLocal = sessionmaker(bind=db_engine)

# Creates the instance of database.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()