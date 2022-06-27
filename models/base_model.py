#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs and len(kwargs) > 0:
            kwargs.pop("__class__")
            for element in kwargs:
                if element == "created_at":
                    self.__dict__[element] = datetime.strptime(kwargs[element], "%Y-%m-%dT%H:%M:%S.%f")
                elif element == "updated_at":
                    self.__dict__[element] = datetime.strptime(kwargs[element], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, element, kwargs[element])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        string = "[" + __class__.__name__ + "]" + " (" + self.id + ") "
        return ("{} {}".format(string, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        for elements in self.__dict__:
            if elements == "created_at":
                self.__dict__[elements] = self.__dict__[elements].isoformat()
            elif elements == "updated_at":
                self.__dict__[elements] = self.__dict__[elements].isoformat()
        self.__dict__["__class__"] = __class__.__name__
        return self.__dict__