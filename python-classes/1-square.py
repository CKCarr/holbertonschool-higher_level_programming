#!/usr/bin/python3
""" module class Square that defines a square by private instance attribute:
size instantiation with size, no imports of other modules allowed """


class Square:
    """ initializes size as private instance attribute"""
    def __init__(self, size):
        self.__size = size
