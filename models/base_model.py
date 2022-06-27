#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime, date
import models
import json
import os
class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) > 0:
            for element in kwargs:
                if element != "__class__":
                    if element == "created_at":
                        kwargs[element] = datetime.fromisoformat(kwargs[element])
                    elif element == "updated_at":
                        kwargs[element] = datetime.fromisoformat(kwargs[element])
                    setattr(self, element, kwargs[element])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        string = "[" + __class__.__name__ + "]" + " (" + self.id + ") "
        return ("{} {}".format(string, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    
    def to_dict(self):
        for elements in self.__dict__:
            if elements == "created_at":
                self.__dict__[elements] = self.__dict__[elements].isoformat()
            elif elements == "updated_at":
                self.__dict__[elements] = self.__dict__[elements].isoformat()
        self.__dict__["__class__"] = __class__.__name__
        return self.__dict__