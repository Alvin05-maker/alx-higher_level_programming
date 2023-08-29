#!/usr/bin/python3
 """Defining a class square"""


 class Square:
     """Representation  of class square"""

     def __init__(self, size=0):
         """initialization of new square .

         Args:
         size(int): the new square size.
         """

         if not isinstance(size, int):
             raise TypeError("size must be an integer")
         elif size < 0:
             raise ValueError("size must be >= 0")
         self._size = size

         def area(self):
             """ area of the new square"""

             return (self.__size * self.__size)
