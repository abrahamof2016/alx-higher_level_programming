#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv)
    sum = 0
    for i in range(1, num_args):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
