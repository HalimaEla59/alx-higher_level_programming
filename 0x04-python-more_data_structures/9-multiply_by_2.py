#!/usr/bin/pthon3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        return dict((k, v * 2) for k, v in a_dictionary.items())
