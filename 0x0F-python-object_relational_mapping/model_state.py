#!/usr/bin/python3
"""
    Contains the class definition of a "State" and an instance Base = declarative_base()
    Models the state object in a MySQL database.
"""

from sqlalchemy import Column, Integer, String
import sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Models a state for a MySQL database

    __tablename__(str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

