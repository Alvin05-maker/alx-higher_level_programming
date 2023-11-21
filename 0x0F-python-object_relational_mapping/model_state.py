#!/usr/bin/python3
"""Model class for the class definition of State"""


from sqlalchemy import Column,Integer,String,MetaData
from sqlalchemy.ext.declarative import declarative_base

custom_metadata = MetaData()
Base = declarative_base(metadata=custom_metadata)

class State(Base):
    """Class definition of the model of the State class."""
    __tablename__= 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

