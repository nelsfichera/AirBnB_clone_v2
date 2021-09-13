#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ Getter for filestorage """
        objDict = models.storage.all(City)
            cities_list = []
            for key, value in objDict.items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return (cities_list)
