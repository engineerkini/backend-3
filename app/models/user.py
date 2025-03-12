from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base  # Import Base from a common base file

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    songs = relationship("Song", back_populates="user")
