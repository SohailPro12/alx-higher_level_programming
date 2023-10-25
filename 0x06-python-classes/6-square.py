#!/usr/bin/python3
"""Module Square."""

class Square:
    """Defines a square class."""

    def __init__(self, size = 0, position(0, 0)):
        """
         Constructor.

         Args:
            size: Length of a side of the square.
            """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for a getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """its a setter for the size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    

    def area(self):
        """Area of this square.

        Returns:
        The size squared.
        """
        return self.__size * self.__size
    
    def my_print(self):
        """hashtags in positions."""
        if self.__size == 0:
            print()
            return
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
