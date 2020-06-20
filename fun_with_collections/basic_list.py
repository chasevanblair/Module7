"""

Program: basic_list.py

Author: Chase Van Blair

Last date modified: 6/19/20


The purpose of this program is to practice using lists
by filling a small list with user input and returning it

"""


def make_list():
    """return list of user input"""
    input_list = []
    for x in range(0, 3):
        input_list.append(get_input())
    return input_list


def get_input():
    """gets one user input then returns it"""
    x = input("Enter number for list: ")
    if x.isnumeric():
        return int(x)
    else:
        raise ValueError
