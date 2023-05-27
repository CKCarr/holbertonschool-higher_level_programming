#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    function that adds all unique integers
    in a list (only once for each integer).
    """
    # set func auto elims dups &stores in variable
    uniq_nums = set(my_list)
    # sum calcs set of unique nums &stores in variable
    total = sum(uniq_nums)
    # returns value
    return (total)
