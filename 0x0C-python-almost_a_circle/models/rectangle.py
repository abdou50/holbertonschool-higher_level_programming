#!/usr/bin/python3
"""class"""
from models.base import Base


class Rectangle(Base):
    """def functions"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """methode"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super() .__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heightmust be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
""""
    def area(self):
        """methode"""

        return self.width * self.height

    def __str__(self):
        """methode"""

        return "[Rectangle] ({}) {}/{} - {}/{}"
        .format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """methode"""

        for i in range(self.hight):
            for j in range(self.width):
                print("#", end="")
            print("")

    def to_dictionary(self):
        """methode"""

        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
"""