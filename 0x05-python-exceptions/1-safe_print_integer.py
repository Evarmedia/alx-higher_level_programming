#!/usr/bin/python3

def safe_print_integer(given_value):
    try:
        print("{:d}".format(given_value))
        return True
    except (TypeError, ValueError):
        return False
