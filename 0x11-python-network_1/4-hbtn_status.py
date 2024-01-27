#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status """

import requests


url = "https://alx-intranet.hbtn.io/status"
body = requests.get(url)
print("Body response:")
print(f"\t- type: {type(body.content.decode('utf-8'))}")
print(f"\t- content: {body.content.decode('utf-8')}")
