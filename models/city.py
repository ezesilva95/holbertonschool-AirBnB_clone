#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class that inherets from BaseModel
    '''
    state_id = ""
    name = ""
