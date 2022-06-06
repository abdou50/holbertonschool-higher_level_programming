#!/usr/bin/python3
""" Rectangle module """
from . base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method
        Args:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """methode"""
        return self.__width

    @property
    def height(self):
        """methode"""
        return self.__height

    @property
    def x(self):
        """methode"""
        return self.__x

    @property
    def y(self):
        """methode"""
        return self.__y

    @width.setter
    def width(self, value):
        """methode"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """methode"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heightmust be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """methode"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """methode"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

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
