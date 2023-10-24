#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the intance attribute and raises exception if error

        Args:
            size (int): Size of the square
            position (tuple): A tuple of two positive number for x and y axis
        """
        Square.check_size(size)
        self.__size = size

        Square.check_pos(position)
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        Square.check_size(value)
        self.__size = value

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        Square.check_pos(value)
        self.__position = value

    def my_print(self):
        """Prints the square using `#` signs"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @staticmethod
    def check_size(size):
        """Checks if the size passed to class Square is valid

        Args:
            size (int): The size of the square at a given instance
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @staticmethod
    def check_pos(position):
        """Checks if the position passed to class Square is valid

        Args:
            position: The position at which the square should be printed
        """

        if type(position) != tuple or len(position) != 2 \
            or type(position[0]) != int or type(position[1]) != int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
