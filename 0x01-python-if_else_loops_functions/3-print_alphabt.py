#!/usr/bin/python3
for index in range(97, 123):
    if chr(index) == 'q' or chr(index) == 'e':
        continue
        print(chr(index).format(index), end='')
