#!/usr/bin/python3
"""
module to print full name.
"""


def say_my_name(first_name, last_name=""):
    """
    arg:
        first_name: a first name(string)
        last_name: a second name(string)
        return: nothing.
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError(
                'first_name must be a string'
                )
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError(
                'last_name must be a string'
                )
    print("My name is" + " " + first_name + " " + last_name)
