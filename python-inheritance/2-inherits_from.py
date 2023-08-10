#!/usr/bin/python3
"""Module to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class
"""

def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj (any): object to be checked
        a_class (any): class to be checked

    Returns:
        bool: True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class