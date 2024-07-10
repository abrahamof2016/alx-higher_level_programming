#!/usr/bin/python3
"""
python module.
contains one function.
"""
def lookup(obj):
    """
    a function.
    arg:
        obj: an object.
    return:
        returns a list of available attributes and methods of an object.
    """
    return(dir(obj))
