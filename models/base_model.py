#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime, date
import models
import json
import os


class BaseModel():
    """
    Define a BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization the attributes of BaseModel
        Args:
            *args: Arguments passed
            **kwargs: Arguments passed with key
        """
        if kwargs is not None and len(kwargs) != 0:
            for elemnt in kwargs:
                if elemnt != "__class__":
                    if elemnt == "created_at":
                        kwargs[elemnt] = datetime.fromisoformat(kwargs[elemnt])
                    elif elemnt == "updated_at":
                        kwargs[elemnt] = datetime.fromisoformat(kwargs[elemnt])
                    setattr(self, elemnt, kwargs[elemnt])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[" + type(self).__name__ + "]" + " (" + self.id + ") "
        return ("{} {}".format(string, self.__dict__))

    def save(self):
        """
        updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        dic = self.__dict__.copy()
        for elements in dic:
            if elements == "created_at":
                dic[elements] = dic[elements].isoformat()
            elif elements == "updated_at":
                dic[elements] = dic[elements].isoformat()
        dic["__class__"] = type(self).__name__
        return dic
