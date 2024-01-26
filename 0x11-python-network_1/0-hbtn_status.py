#!/usr/bin/python3
#  fetches https://alx-intranet.hbtn.io/status

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    utf8_html = html.decode('utf8')
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(utf8_html))
