from sqlalchemy import Column, Integer, String, BIGINT
from .database_manager import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    national_id = Column(BIGINT, nullable=False)

