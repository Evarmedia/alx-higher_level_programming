#!/usr/bin/python3

def safe_print_list(main_list =[], x=0):
    index = 0
    for index in range(x):
        try:
            print(main_list[index], end='')
            index += 1
        except IndexError:
            break
    print()
    return index
