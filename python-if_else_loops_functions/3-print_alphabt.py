#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) not in 'q' and chr(letter) not in 'e':
        print("{}".format(chr(letter)), end="")
