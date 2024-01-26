#!/usr/bin/python3
"""Sends a request to given url_target and
displays the body of the response in utf-8
Error handling is allowed here
"""

from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


def print_body_n_fix_err():
    """Prints the body of the response from a server in utf-8"""
    url_target = argv[1]
    reqst = Request(url_target)

    try:
        with urlopen(reqst) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except URLError as err:
        if hasattr(err, 'code'):
            print(f"Error code: {err.code}")
        elif hasattr(err, 'reason'):
            print(f"Error reason: {err.reason}")
        else:
            print(f"{err}")


if __name__ == "__main__":
    print_body_n_fix_err()
