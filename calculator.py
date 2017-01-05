"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def is_input_valid(token_list):
    for token in token_list[1:]:
        if token in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        else:
            return False

# Your code goes here
while True:
    user_input = raw_input("prefix equation: >  ")
    token_list = user_input.split(' ')
    #print token_list
    token_list = [x for x in token_list if x != '']  # Strip all spaces          
    #print token_list
    if token_list[0] == 'q':
        break
    else:
        if is_input_valid(token_list):
            if token_list[0] == '+':
                print add(int(token_list[1]), int(token_list[2]))
            elif token_list[0] == '-':
                print subtract(int(token_list[1]), int(token_list[2]))
            elif token_list[0] == '*':
                print multiply(int(token_list[1]), int(token_list[2]))
            elif token_list[0] == '/':
                print divide(int(token_list[1]), int(token_list[2]))
            elif token_list[0] == 'square':
                print square(int(token_list[1]))
            elif token_list[0] == 'cube':
                print cube(int(token_list[1]))
            elif token_list[0] == 'power':
                print power(int(token_list[1]), int(token_list[2]))
            elif token_list[0] == 'mod':
                print mod(int(token_list[1]), int(token_list[2]))
            else:
                print token_list[0] + " is not a valid operation. Try again."
        else:
            print "That is not a valid input"
