#!/usr/bin/python3
"""This module uses `requests` to send a GET request to the URL"""

import requests


def get_url():
    """Fetches data from the given_url `https://alx-intranet.hbtn.io/status`"""
    given_url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(given_url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}\n\t- content: {response.text}")


if __name__ == "__main__":
    get_url()
