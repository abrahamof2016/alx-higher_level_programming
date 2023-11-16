#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set(my_list)
    sum = 0
    for element in result:
        sum += element
    return sum
