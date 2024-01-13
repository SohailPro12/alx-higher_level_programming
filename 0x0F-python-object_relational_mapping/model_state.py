#!/usr/bin/python3

"""
the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
