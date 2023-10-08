#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = tuple_a[0] if len(tuple_a) >= 1 else 0 # Get the first element of tuple_a or use 0 if it is missing
    y1 = tuple_a[1] if len(tuple_a) >= 2 else 0 # Get the second element of tuple_a or use 0 if it is missing
    x2 = tuple_b[0] if len(tuple_b) >= 1 else 0 # Get the first element of tuple_b or use 0 if it is missing
    y2 = tuple_b[1] if len(tuple_b) >= 2 else 0 # Get the second element of tuple_b or use 0 if it is missing
    return (x1 + x2, y1 + y2) # Return a tuple with the sums of corresponding elements
