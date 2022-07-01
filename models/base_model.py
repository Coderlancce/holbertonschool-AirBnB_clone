#!/usr/bin/python3
"""This module contains a class BaseModel that defines all
   common attributes/methods for other classes.
"""


class BaseModel:
    """This is an abstract class that defines attributes
    for other classes.
    """
    def __init__(self, id):
        """Initialize the object

        Args:
            id (string): Unique id of the object
        """
        self.id = id
