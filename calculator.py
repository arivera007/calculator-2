"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("prefix equation: >  ")
    token_list = user_input.split(" ")
    if token_list[0] == 'q':
        break
    else:
        if token_list[0] == '+':  # Culturally using double quotes is used for messages
            print add(int(token_list[1]), int(token_list[2]))
        elif token_list[0] == "-":
            print subtract(int(token_list[1]), int(token_list[2]))
        elif token_list[0] == "*":
            print multiply(int(token_list[1]), int(token_list[2]))
        elif token_list[0] == "/":
            print divide(int(token_list[1]), int(token_list[2]))
        elif token_list[0] == "square":
            print square(int(token_list[1]))
        elif token_list[0] == "cube":
            print cube(int(token_list[1]))
        elif token_list[0] == "power":
            print power(int(token_list[1]), int(token_list[2]))
        elif token_list[0] == "mod":
            print mod(int(token_list[1]), int(token_list[2]))
        else:
            print token_list[0] + " is not a valid operation. Try again."
