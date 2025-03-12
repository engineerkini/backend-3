from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.base import Base  # Import Base

DATABASE_URL = "postgresql+psycopg2://user:password@localhost/spotify_db"
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/spotify_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
