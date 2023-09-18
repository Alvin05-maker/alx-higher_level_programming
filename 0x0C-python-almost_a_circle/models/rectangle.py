#!/usr/bin/python3
""" Define a class Rectangle."""
from  models.base import Base


class Rectangle(Base):
	""" Represemtation of a class Rectangle.
	This class inherits from the the Base class.
	Base: The parent(base) class
	"""
	def __init__(self, width, height, x=0, y=0, id=None):
		""" Initialize a new rectangle.
		
		Args:
			width(int): the width of the rectangle.
			height(int): the height of the new rectangle.
			x(int): the x coordinate of the new rectangle.
			y(int): the y coordinate of the new rectangle.
			id(int): the id of the new rectangle.
		Raises:
			TypeError: If either of width or height is not an int.
			ValueError: If either of width or height <= 0.
			TypeError: If either of x or y is not an int.
			ValueError: If either of x or y < 0.
		"""
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		super().__init__(id)
	@property
	def width(self):
		"""Get/set the width of the Rectangle."""
		return self.__width
	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value
	@property
	def height(self):
		""" Get/set the height of the Rectangle"""
		return self.__height
	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value
	@property
	def x(self):
		""" Get/set the x coordinate of  Rectangle"""
		return self.__x
	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value
	@property
	def y(self):
		""" Get/Set the y coordinate of Rectangle."""
		return self.__y
	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value
	def area(self):
		"""  Find the area of rectangle."""
		return self.width * self.height
	def display(self):
		"""Print the Rectangle using the `#` character."""
		if self.width == 0 or self.height == 0:
			print("")
			return
		[print("") for y in range(self.y)] # positioning the vertical starting point of the rectangle
		for height in range(self.height):
			[print(" ", end="") for x in range(self.x)] # positioning  the horizontal starting point
			[print("#", end="") for w in range(self.width)]
			print("")
	def __str__(self):
		""" Return print() and str() representation of rectangle."""
		return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
