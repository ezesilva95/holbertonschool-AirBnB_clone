#!/usr/bin/python3
import json
import os
class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path) as f:
                json.load(f)