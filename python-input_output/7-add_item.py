#!/usr/bin/python3

""" This script adds all arguments to a Python list and saves them to a file.
It uses the save_to_json_file function from 5-save_to_json_file.py and the
load_from_json_file function from 6-load_from_json_file.py.
The list is saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it is created. The script does not handle file
permissions or exceptions.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Read existing data from add_item.json or create an empty list
try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

# Append the command-line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to add_item.json
save_to_json_file(data, filename)

# Print the updated list
print(data)
