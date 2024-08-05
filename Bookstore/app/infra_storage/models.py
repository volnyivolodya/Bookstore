from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    publish_year = Column(Integer, nullable=False)
    pages_count = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False)