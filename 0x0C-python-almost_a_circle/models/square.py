#!/usr/bin/python3
""" the square """

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init methode"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """methode to write"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        """getter methode."""

        return self.__width

    @size.setter
    def size(self, value):
        """setter methode"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """args and kwargs"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                for j in kwargs.keys():
                    if j == "id":
                        self.id = kwargs["id"]
                    if j == "size:
                        self.size = kwargs["size"]
                    if j == "x":
                        self.x = kwargs["x"]
                    if j == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """set it to dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
