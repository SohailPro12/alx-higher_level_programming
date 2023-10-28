#!/usr/bin/python3
"""Module contain one method text_identation"""


def text_indentation(text):
    """method that print a new line

    Args:
        text: the text
        i: for iterations
    """

    for i in text:
        if i == "." or i =="?" or i == ":":
            print(i)
            print('')
            continue
        print(i, end = '')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
