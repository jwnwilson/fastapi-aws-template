from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseSQLModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
