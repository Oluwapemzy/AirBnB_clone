#!usr/bin/python3
"""
Base Module for AirBnB clone Project
"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
    BaseModel Class
    """
    def __init__(self):
        """
        Initializes the class BaseModel
        """
        self.id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """return str representation"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dict"""
        gdict = delf.__dict__.copy()
        gdict["created_at"] = self.created_at.isoformat()
        gdict["updated_at"] = self.updated_at.isoformat()
        gdict["__class__"] = self.__class__.__name__
        return gdict
