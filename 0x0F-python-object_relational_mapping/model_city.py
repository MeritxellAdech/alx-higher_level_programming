#!/usr/bin/python3
""" This module has the definition of the city model """
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Definition of the model, city"""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", backref="cities")
