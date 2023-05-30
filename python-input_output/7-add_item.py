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
import importlib

# Use importlib to import modules with non-standard names
save_to_json_file = (
    importlib.import_module('5-save_to_json_file').save_to_json_file
)
load_from_json_file = (
    importlib.import_module('6-load_from_json_file').load_from_json_file
)

filename = "add_item.json"

# Try to load the list from the file, or create a new one if it doesn't exist
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(my_list, filename)
