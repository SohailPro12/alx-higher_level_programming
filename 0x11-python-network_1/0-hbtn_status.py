#!/usr/bin/python3
#  fetches https://alx-intranet.hbtn.io/status

from urllib import request, error



url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()
    body_decoded = body.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body_decoded))
