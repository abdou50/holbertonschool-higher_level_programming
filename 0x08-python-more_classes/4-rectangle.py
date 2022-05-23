#!/usr/bin/python3
""" class """


class Rectangle:
    """Rectangle ."""

    def __init__(self, width=0, height=0):
        """class
        """
        self.width = width
        self.height = height

    def __str__(self):
        """string """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """R
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """wight"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setsr
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height ."""
        return self.__height

    @height.setter
    def height(self, value):
        """tttttttttt
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ttttttt
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        jjjjj
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
