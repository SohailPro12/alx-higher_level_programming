#!/usr/bin/python3
"""Module Square."""

class Square:
    """Defines a square class."""

    def __init__(self, size = 0):
        """
         Constructor.

         Args:
            size: Length of a side of the square.
            """
        self.size = size

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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
        The size squared.
        """
        return self.__size * self.__size
