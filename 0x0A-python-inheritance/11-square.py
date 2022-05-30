#!/usr/bin/python3
""" class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class """
    def __init__(self, size):
        """ class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
