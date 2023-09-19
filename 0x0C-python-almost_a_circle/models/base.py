#!/usr/bin/python3
""" Define a class base"""
import json
import csv


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
	@staticmethod
	def to_json_string(list_dictionaries):
		""" Return the serialization of list of dictionaries to JSON string.

		Args:
			list_dictionaries(dict): list of dictionaries.
		"""
		if list_dictionaries is None or list_dictionaries == []:
			return "[]"
		return json.dumps(list_dictionaries)
	@classmethod
	def save_to_file(cls, list_objs):
		"""Write the JSON serialization of a list of objects to a file.

		Args:
			list_objs (list): A list of inherited Base instances.
		"""
		filename = cls.__name__ + ".json"
		with open(filename, "w") as jsonfile:
			if list_objs is None:
				jsonfile.write("[]")
			else:
				list_dicts = [o.to_dictionary() for o in list_objs]
				jsonfile.write(Base.to_json_string(list_dicts))
	@staticmethod
	def from_json_string(json_string):
		"""Return the deserialization of a JSON string.

		Args:
			json_string (str): A JSON str representation of a list of dicts.
		Returns:
			If json_string is None or empty - an empty list.
			Otherwise - the Python list represented by json_string.
		"""
		if json_string is None or json_string == "[]":
			return []
		return json.loads(json_string)
