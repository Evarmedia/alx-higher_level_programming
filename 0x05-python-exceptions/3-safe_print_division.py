#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        final_result = a / b
    except ZeroDivisionError:
        final_result = None
    finally:
        print("Inside result: {}".format(final_result))
        return final_result
