#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary.items())
    for i in a_dictionary:
        print("{}: {}".format(i[0], i[1]))
