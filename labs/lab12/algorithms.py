"""
Name: Maddie Reed
algorithms.py

Problem: This program organizes data and sorts into a single list.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(file_name):
    my_file = open(file_name, 'r')
    line = my_file.readlines()
    len_of_file = len(line)
    i = 0
    num_list = []
    while i < len_of_file:
        line_list = line[i].split()
        len_of_line_list = len(line_list)
        i += 1
        j = 0
        while j < len_of_line_list:
            line_list[j] = eval(line_list[j])
            num_list += [line_list[j]]
            j += 1
    my_file.close()
    return num_list


def is_in_linear(search_val, values):
    i = 0
    tally = 0
    while i < len(values):
        if values[i] == search_val:
            tally += 1
            i += 1
        else:
            i += 1
    if tally > 0:
        return True
    else:
        return False
