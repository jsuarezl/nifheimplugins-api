from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    url = Column(String, unique=True, nullable=False)
    version = Column(String, nullable=False)
    last_updated = Column(DateTime, nullable=True)
