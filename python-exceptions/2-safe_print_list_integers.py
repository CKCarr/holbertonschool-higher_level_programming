#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_integers = 0
    for idx in range(x):
        try:
            # assign list index to check the value of the index
            val = my_list[idx]
            # check if idx value is an integer in each instance
            if isinstance(val, int):
                # integers have to be printed on the same line
                print("{:d}".format(val), end="")
                # update count by one to increment loop
                num_integers += 1
        # handle exceptions
        except IndexError:
            break # skip if index is not an int till end of list
    print()  # print newline
    return num_integers
