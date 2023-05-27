#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for data in my_list:
        if data == search:
            new_list.append(replace)
        else:
            new_list.append(data)
    return (new_list)
