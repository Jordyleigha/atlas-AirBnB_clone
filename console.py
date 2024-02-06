#!/usr/bin/env python3
"""Console for the application. """
import cmd

import models
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Class that contains the console for the application.
    """

    prompt = '(hbnb) '
    __classes = {'BaseModel': BaseModel, 'User': User,
                 'State': State, 'City': City, 'Amenity': Amenity,
                 'Place': Place, 'Review': Review}

    def do_create(self, *args):
        """
        Creates an instance of a class
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(args[0] + "." + str(eval(args[0] + "()")))
