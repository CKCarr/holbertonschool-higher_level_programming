#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_ints = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_ints += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print()
    return num_ints

