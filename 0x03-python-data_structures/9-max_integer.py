#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        r = my_list[0]
        for i in my_list[1:]:
            if i > r:
                r = i
        return r
