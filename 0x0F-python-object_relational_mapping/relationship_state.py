#!/usr/bin/python3
"""
Script--> Defines class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class State with instance of Base
    linked to MySQL--> table "states"
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
