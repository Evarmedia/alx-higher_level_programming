#!/usr/bin/python3
"""This module contains code to display body of response if successful"""

import requests
from sys import argv


def fixinf_errors():
    """Sends a `GET` request to a ur_url and displays the body of the response
    only if the response code is less than 400
    """

    ur_url = argv[1]
    try:
        response = requests.get(ur_url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    fixinf_errors()
