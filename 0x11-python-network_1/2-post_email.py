#!/usr/bin/python3
"""This module contains code to `POST` an email to a url passed as argument
unfortunately, they don't permit error handling
"""

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
