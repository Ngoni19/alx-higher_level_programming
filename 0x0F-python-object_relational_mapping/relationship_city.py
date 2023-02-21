#!/usr/bin/python3
"""
Script--> Defines class City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State



class City(Base):
    """
    Class City with instance of Base
    linked to MySQL--> table "city"
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)  # auto-add
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
