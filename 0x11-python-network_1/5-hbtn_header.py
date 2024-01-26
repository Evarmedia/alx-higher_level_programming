#!/usr/bin/python3
"""Displays the value of header X-Request-Id in response in given URL"""

import requests
from sys import argv


def printing_x_request_id():
    """Prints value of `X-Request-Id` using `requests` and a given URL"""

    target_url_ = argv[1]
    try:
        response = requests.get(target_url_)
        response.raise_for_status()
        print(response.headers.get('X-Request-Id'))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    printing_x_request_id()
