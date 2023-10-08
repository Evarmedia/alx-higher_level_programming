#!/usr/bin/python3
def no_c(my_string):
    new_str_ = ""
    for char in my_string:
        if char not in ('c', 'C'):
            new_str_ += char
    return new_str_
