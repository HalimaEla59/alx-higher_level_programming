#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        copy = my_list.copy()
        return copy
    del my_list[idx]
    copy = my_list.copy()
    return copy
