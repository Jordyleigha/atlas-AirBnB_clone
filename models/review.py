#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review with the inheritance from Base"""
    place_id = ''
    user_id = ''
    text = ''
