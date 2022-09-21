#!/usr/bin/python3
'''Rectangle class'''


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not (isinstance(height, int)):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function for private attribute width
            Args:
                value: size value to set to.
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns width of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for private attribute width
            Args:
                value: size value to set to.
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """
        If width or height = 0, return 0
        Else return perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
        
