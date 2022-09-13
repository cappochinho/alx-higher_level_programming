#!/usr/bin/python3


class Square:
    """Square() class with public instance method"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
            
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
            
    def my_print(self):
        """prints square using #"""
        s = self.__size
        if s == 0:
            print()
        else:
            i, j = 0, 0
            for i in range(self.__position[1]):
                print()
            for j in range(s):
                print("{}{}".format(" " * self.__position[0], "#" * s))
                
    def position(self):
        return self.__position
    
    def position(self, value):
        if value[0] < 0 | value[1] < 0:
            raise TypeError("position must a tuple of 2 positive integers")
        else:
            self.__position = value

        
