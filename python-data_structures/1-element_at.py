#!/usr/bin/python3
""" check if idx is negative or greater than or equal to the length of my_list"""
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return (None)
    return (my_list[idx])
