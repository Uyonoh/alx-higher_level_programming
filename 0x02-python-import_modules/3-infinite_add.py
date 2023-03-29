#!/usr/bin/python3

import sys

def infinite_add():
    sums = 0
    i = 1

    while i < len(sys.argv):
        try:
            sums += int(sys.argv[i])
        except ValueError:
            pass
        i += 1

    print(sums)


if __name__ == "__main__":
    infinite_add()
