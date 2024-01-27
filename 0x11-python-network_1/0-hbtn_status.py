#!/usr/bin/python3

"""fetches the url"""

from urllib import request, error


url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()
    body_decoded = body.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print("\t- utf8 content: {}".format(body_decoded))
