#!/usr/bin/python3
"""
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.status))
