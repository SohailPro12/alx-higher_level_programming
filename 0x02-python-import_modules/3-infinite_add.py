#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    addition = 0
    for i in range(0, len(sys.argv) - 1):
        addition += int(args[i])
    print("{}".format(addition))
