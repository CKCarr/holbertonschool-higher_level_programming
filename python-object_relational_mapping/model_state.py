#!/usr/bin/python3
"""
    This script contains the class definition of a State
    and an instance Base = declarative_base():
    to work with MySQLAlchemy ORM.
"""

from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
