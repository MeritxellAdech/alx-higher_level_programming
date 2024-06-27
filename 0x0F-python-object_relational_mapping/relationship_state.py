#!/usr/bin/python3
"""
Implementing ORMs using sqlachemy to interact with the database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines the structure of a table in a db"""

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    # Relationship with City
    cities = relationship("City", backref="state", cascade="all")
