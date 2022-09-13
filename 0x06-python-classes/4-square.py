#!/usr/bin/python3


class Square:
    """Square() class with public instance method"""
    def __init__(self, size=0):
        self.__size = size
            
    def area(self):
        return self.__size ** 2
      
    def size(self):
        return self.__size
    
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
