#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
    return result
