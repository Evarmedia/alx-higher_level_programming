#!/usr/bin/python3
"""This module contains code which displays value of `X-Request-Id` variable
"""

from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


def print_header_val():
    """This function prints the `X-Request-Id` value in the response header of
    the_target_url passed in as first argument
    """

    the_target_url = argv[1]
    made_req = Request(the_target_url)

    try:
        with urlopen(made_req) as response:
            response_header = response.info()
    except URLError as err:
        if hasattr(err, 'reason'):
            print('We failed to reach a server.')
            print("Reason: ", err.reason)
        elif hasattr(err, 'code'):
            print("The server couldn't fulfill the request.")
            print("Error code: ", err.code)
        exit(1)

    if response_header.get('X-Request-Id'):
        print(response_header['X-Request-Id'])


if __name__ == "__main__":
    print_header_val()
