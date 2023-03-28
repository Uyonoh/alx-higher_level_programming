#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    my_list = []

    while i < list_length:
        n = 0
        try:
            n = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_list.append(n)
            i += 1
    return my_list
