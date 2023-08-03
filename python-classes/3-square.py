#Documentation

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
    def area(self):
        """Return area of square"""
        return self.__size ** 2
    @property
    def size(self):
        """Retrieve size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0: 
            raise ValueError("size must be >= 0")