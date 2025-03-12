from sqlalchemy import create_engine
from sqlalchemy.engine import URL

DATABASE_URL = "postgresql+psycopg2://user:password@localhost/spotify_db"

engine = create_engine(DATABASE_URL)
