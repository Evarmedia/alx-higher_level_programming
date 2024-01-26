#!/usr/bin/python3
"""This module contains code to `POST` an ur_email to a ur_url passed as argument
"""

import requests
from sys import argv


def post_email_to_server():
    """Sends an ur_email to a server"""

    ur_url = argv[1]
    ur_email = argv[2]
    payload = {"email": ur_email, }
    response = requests.post(ur_url, data=payload)
    if response.status_code == 200:
        print(response.text)
    else:
        print("[{}] {}".format(response.status_code, response.text))


if __name__ == "__main__":
    post_email_to_server()
