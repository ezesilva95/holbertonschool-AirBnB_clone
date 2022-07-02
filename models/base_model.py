#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime, date
import models
import json
import os


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for elemnt in kwargs:
                if elemnt != "__class__":
                    if elemnt == "created_at":
                        kwargs[elemnt] = datetime.fromisoformat(kwargs[elemnt])
                    elif element == "updated_at":
                        kwargs[elemnt] = datetime.fromisoformat(kwargs[elemnt])
                    setattr(self, elemnt, kwargs[element])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        string = "[" + type(self).__name__ + "]" + " (" + self.id + ") "
        return ("{} {}".format(string, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        for elements in dic:
            if elements == "created_at":
                dic[elements] = dic[elements].isoformat()
            elif elements == "updated_at":
                dic[elements] = dic[elements].isoformat()
        dic["__class__"] = type(self).__name__
        return dic
