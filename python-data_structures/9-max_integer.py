#!/usr/bin/python3
def max_integer(my_list=[]):
    # if list empty, return none
    if len(my_list) == 0:
        return (None)
    # initialize variable to store max num of list
    max_num = my_list[0]
    # iterate through list
    for num in my_list[1:]:
        # if current num is greater than current max
        if num > max_num:
            # update variable to store new max num
            max_num = num
    # return the final max num
    return (max_num)
