#!/usr/bin/python3
import uuid
from datetime import datetime

"""
  A class BaseModel that defines all common attributes/methods for other classes:
"""

class BaseModel:
  """"
    Write a class BaseModel that defines all common attributes/methods for other classes
  """
  def __init__(self) -> None:
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

  def __str__(self):
   return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
  
  def save(self):
    self.updated_at = datetime.now()

  def to_dict(self):
    obj_dict = self.__dict__.copy()
    obj_dict["__class__"] = type(self).__name__
    obj_dict["created_at"] = self.created_at.isoformat()
    obj_dict["updated_at"] = self.updated_at.isoformat()
    return obj_dict