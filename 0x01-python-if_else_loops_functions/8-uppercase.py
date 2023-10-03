#!/usr/bin/python3
def uppercase(c):
    for char in c:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print(char, end="")
    print("")

