#!/usr/bin/python3
"""
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code < 400:
        content = response.text
        print(content)
    else:
        print("Error code: {}".format(response.status))
