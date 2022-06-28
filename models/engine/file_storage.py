#!/usr/bin/python3
import json
from logging import exception
import os
import models

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        tmp = {}
        for key in FileStorage.__objects.keys():
            tmp[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'a+', encoding='utf-8') as f:
            json.dump(tmp, f)
    
    def reload(self):
        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
                obj = json.load(f)