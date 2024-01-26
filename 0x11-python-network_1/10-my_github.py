#!/usr/bin/python3
"""Authenticates a userName and id using github api"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def fetch_the_github_id():
    """Displays the github id of the userName"""
    if len(argv) < 3:
        print(f"usage: {argv[0]} <username> <password>")
        exit(1)

    userName, usr_passwd = argv[1], argv[2]
    url = "https://api.github.com/userName"
    auth = HTTPBasicAuth(userName, usr_passwd)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        print(response.json().get("id"))
    except requests.exceptions.HTTPError:
        print("None")
    except requests.exceptions.JSONDecodeError as e:
        print(f"not a valid JSON: {e}")
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")


if __name__ == "__main__":
    fetch_the_github_id()
