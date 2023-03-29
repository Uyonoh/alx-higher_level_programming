#!/usr/bin/python3

import add_0

def add_num():
    a = 1
    b = 2

    sums = add_0.add(a, b)
    print("{} + {} = {}".format(a, b, sums))

if __name__ == "__main__":
    add_num()
