# Documentation: https://docs.python.org/3/tutorial/classes.html#class-objects

"""This is a square class"""
class Square:
    """Square class with private attribute"""
    def __init__(self, size=0):
        """Initialize data"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0: 
            raise ValueError("size must be >= 0")