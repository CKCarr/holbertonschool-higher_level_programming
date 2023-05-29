#!/usr/bin/python3
""" This script adds all arguments to a Python list and saves them to a file.
It uses the save_to_json_file function from 5-save_to_json_file.py and the
load_from_json_file function from 6-load_from_json_file.py.
The list is saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it is created. The script does not handle file
permissions or exceptions. """
import sys
import os.path

"""Import functions from other python files
__import__() used because standard import statement doesn't work
with filenames starting with a number. """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Initialize an empty list
my_list = []

# Check if the file "add_item.json" exists
if os.path.isfile("add_item.json"):
    # If the file exists, load the data from the file
    my_list = load_from_json_file("add_item.json")

# Loop through the command line args starting from index 1, exclude script name
for i in range(1, len(sys.argv)):
    # Append each argument to the list
    my_list.append(sys.argv[i])

# Save the updated list back to the file
# If the file doesn't exist, it will be created at this point.
save_to_json_file(my_list, "add_item.json")
