#!/usr/bin/python3
"""class"""


class Base:
	__nb_objects = 0
	"""def function init """
	def __init__(self, id=None):
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = self.__nb_objects