"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
import argparse

parser = argparse.ArgumentParser(description='Prefix calculator')
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
        if token_list[0] == '+':
            print add(token_list[1:])
        elif token_list[0] == '-':
            print subtract(token_list[1:])
        elif token_list[0] == '*':
            print multiply(token_list[1:])
        elif token_list[0] == '/':
            print divide(token_list[1:])
        elif token_list[0] == 'square':
            print square(int(token_list[1]))
        elif token_list[0] == 'cube':
            print cube(int(token_list[1]))
        elif token_list[0] == 'power':
            print power(token_list[1:])
        elif token_list[0] == 'mod':
            print mod(token_list[1:])
        else:
            print token_list[0] + " is not a valid operation. Try again."
