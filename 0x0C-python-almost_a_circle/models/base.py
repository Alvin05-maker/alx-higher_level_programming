#!/usr/bin/python3
""" Define a class base"""


class Base:
	"""Representation of class Base .
	This is the base model of all the clasees in this project.

	Private class attributes:
		__nb_objects(int): No of instantiated  base objects.
	"""
	__nb_objects = 0
	def __init__(self, id=None):
		""" Initialize the new base object.
	
		Args:
			id(int): the id of the instance Base object.
		"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
