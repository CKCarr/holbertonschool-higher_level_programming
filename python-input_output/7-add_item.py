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

# Load the code from file as a string
with open("5-save_to_json_file.py", "r") as file:
    save_to_json_code = file.read()

with open("6-load_from_json_file.py", "r") as file:
    load_from_json_code = file.read()

# Execute the module code and capture the resulting global variables in {}
save_to_json_globals = {}
exec(save_to_json_code, save_to_json_globals)

load_from_json_globals = {}
exec(load_from_json_code, load_from_json_globals)

# Access the functions from the global dictionary
save_to_json_file = save_to_json_globals["save_to_json_file"]
load_from_json_file = load_from_json_globals["load_from_json_file"]
# function takes a list of command line arguments


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
