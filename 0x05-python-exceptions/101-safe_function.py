#!/usr/bin/python3
def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as er:
        print("Exception: {}".format(er))
    return result
