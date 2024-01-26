#!/usr/bin/python3
"""This module contains code to fetch data from `https://alx-intranet.hbtn.io/status`"""
import urllib.request
import sys

def fetch_x_request_id(url):
    """Send a request to the URL and display the value of the X-Request-Id variable"""
    req = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(req) as response:
            x_request_id = response.getheader('X-Request-Id')
            print("Value of X-Request-Id variable:", x_request_id)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print("Failed to reach the server. Reason:", e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn't fulfill the request. Error code:", e.code)

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_x_request_id(url)
