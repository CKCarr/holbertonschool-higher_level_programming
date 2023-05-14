#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Using list comprehension to iterate over my_list
    and check if each element is divisible by 2"""
    return [num % 2 == 0 for num in my_list]
