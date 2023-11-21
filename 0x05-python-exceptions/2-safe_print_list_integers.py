#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_char = 0
    for i in my_list:
        if printed_char == x:
            break
        try:
            print("{:d}".format(i), end="")
            printed_char+=1
        except Exception:
            pass
    print()
    return printed_char
