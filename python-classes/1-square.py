# This file is part of python-classes
# Docstrings are not necessary for public methods, but you should have a docstring for every module, class, and function.

class Square:
    """Square class with private attribute"""
    def __init__(self, size=0):
        """Initialize data"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0: 
            raise ValueError("size must be >= 0")