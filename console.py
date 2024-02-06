#!/usr/bin/env python3
""" Console for the application. """
import cmd

import models
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.stae import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
