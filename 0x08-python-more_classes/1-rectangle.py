#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """ class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    '''property'''
    @property
    def width(self):
        return self.__width
    '''setter'''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    '''property'''
    @property
    def height(self):
        return self.__height
    '''setter'''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
