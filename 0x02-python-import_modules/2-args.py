#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("1: {}".format(args[0]))
    elif len(sys.argv) - 1 ==0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(0, len(sys.argv) - 1):
            print("{}: {}".format(i+1, args[i]))
