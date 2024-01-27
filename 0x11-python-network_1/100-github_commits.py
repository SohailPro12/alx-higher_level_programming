#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

import requests
import sys


if __name__ == "__main__":
    rep = sys.argv[1]
    own = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
                     rep, own)

    r = requests.get(url)
    j = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                j[i].get("sha"),
                j[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
