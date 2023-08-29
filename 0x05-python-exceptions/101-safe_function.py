#!/usr/cin/python3

def safe_function(fct, *args):
    import sys

    try:
        res = fct(*args)
        return res
    except:
        sys.stderr.write("Exception: {}\n".format(sys.exec_info()[1]))
        return None
