#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        
        Square.check_size(size)
        self.__size = size

        Square.check_pos(position)
        self.__position = position

    @property
    def size(self):
        """:obj:`int`: Current size of the square

        The setter method raises an exception if the value is not int or < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        Square.check_size(value)
        self.__size = value

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: index 0 sets spaces and 1 sets newline

        The setter method raises an exception of ValueError or TypeError
        """
        return self.__position

    @position.setter
    def position(self, value):
        Square.check_pos(value)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        disp_sqr = ""
        if self.__size == 0:
            return disp_sqr
        else:
            x, y = self.__position

            for _ in range(y):
                disp_sqr = disp_sqr + "\n"

            for _ in range(self.__size):
                if x:
                    disp_sqr = disp_sqr + (' ' * x)
                disp_sqr += ('#' * self.__size) + '\n'
            disp_sqr = disp_sqr[:-1]
            return disp_sqr

    @staticmethod
    def check_size(size):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @staticmethod
    def check_pos(position):

        if type(position) != tuple or len(position) != 2 \
            or type(position[0]) != int or type(position[1]) != int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
