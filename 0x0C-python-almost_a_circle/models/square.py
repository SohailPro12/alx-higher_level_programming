#!/usr/bin/python3

"""
A module with the class Square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square object that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initilaize the attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str implementation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
