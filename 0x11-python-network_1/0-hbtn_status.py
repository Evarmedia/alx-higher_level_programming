#!/usr/bin/python3
"""This module contains the code to data fetch `https://alx-intranet.hbtn.io/status`"""

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def fetch_body():
    """Fetches the site and the body"""
    target_url = "https://alx-intranetbtn.io/status"
    request = Request(target_url)

    try:
        response = urlopen(request)
        response_body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))
    except HTTPError as error:
        print("Error code: ", error.code)
    except URLError as error:
        print("Reason: ", error.reason)

if __name__ == "__main__":
    fetch_body()
