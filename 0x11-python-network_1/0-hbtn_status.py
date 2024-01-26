#!/usr/bin/python3
"""This module contains the code to data fetch `https://alx-intranet.hbtn.io/status`"""

import urllib.request

url = 'https://alx-inet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print('- Body response:')
    print('\t- type:', type(body))
    print('\t- content:', body)
    print('\t- utf8 content:', body.decode('utf-8'))

except Exception as e:
    print('An error occurred:', e)
