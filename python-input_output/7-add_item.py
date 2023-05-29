#!/usr/bin/python3

""" This module writes a script that adds all arguments to a Python list,
and then save them to a file.
You must use your function save_to_json_file from 5-save_to_json_file.py.
You must use your function load_from_json_file from 6-load_from_json_file.py.
The list must be saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it should be created
Does not manage file permissions / exceptions.
"""

import sys
import imp

# Import module "5-save_to_json_file.py"
save_to_json_module = imp.load_source("save_to_json_file",
                                      "./5-save_to_json_file.py")
save_to_json_file = save_to_json_module.save_to_json_file

# Import module "6-load_from_json_file.py"
load_from_json_module = imp.load_source("load_from_json_file",
                                        "./6-load_from_json_file.py")
load_from_json_file = load_from_json_module.load_from_json_file


def add_args_to_list(args):
    """ Function that adds all command line arguments to a Python List.

    Args:
        args (list): The command line arguments to be added to the list.
    Return: (list): The updated list.
    Raises: None
    """
    # 'data' read from JSON file and stored in variable
    try:
        data = load_from_json_file('add_item.json')
    # If the file doesn’t exist, it should be created
    except FileNotFoundError:
        data = []

    # extend method is used to append multiple elements to a list.
    data.extend(args)
    # save the updated list to JSON representation in a file
    save_to_json_file(data, "add_item.json")
    return data


# Extract command line arguments excluding the script name argv[1:...]
args = sys.argv[1:]
# Add args to list, and save updated list to add_item.json
updated_arg_list = add_args_to_list(args)
print(updated_arg_list)
