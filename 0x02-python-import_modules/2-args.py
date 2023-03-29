#!/usr/bin/python3

import sys

def args():
    print(str(len(sys.argv) - 1), end="")
    if len(sys.argv) == 2:
        print(" argument:")
    else:
        print(" arguments", end="")
        
        if len(sys.argv) == 1:
            print(".")
        else:
            print(":")

    i = 1
    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1


if __name__ == "__main__":
    args()

