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
# 'data' read from JSON file and stored in variable
try:
    data_to_file = load_from_json_file(filename)
# If the file doesn’t exist, it should be created
except FileNotFoundError:
    data_to_file = []
# extend method is used to append multiple elements to a list.
data_to_file.extend(sys.argv[1:])
# list 'data' must be saved as a JSON rep in a file
save_to_json_file(data_to_file, filename)
