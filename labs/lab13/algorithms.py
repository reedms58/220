"""
Name: Maddie Reed
algorithms.py

Problem: This program organizes data and sorts into a single list.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


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


def selection_sort(values):
    for j in range(len(values)):
        for i in range(j, len(values)):
            minimum = values[j]
            if values[i] < minimum:
                min_index = values.index(minimum)
                values[i], values[min_index] = values[min_index], values[i]


def calc_area(rect):
    point_one, point_two = rect.getP1(), rect.getP2()
    x_point_one, y_point_one = point_one.getX(), point_one.getY()
    x_point_two, y_point_two = point_two.getX(), point_two.getY()
    side_one = abs(x_point_two - x_point_one)
    side_two = abs(y_point_two - y_point_one)
    area = side_one * side_two
    return area


def rect_sort(rectangles):
    for j in range(len(rectangles)):
        for i in range(j, len(rectangles)):
            minimum = calc_area(rectangles[j])
            if calc_area(rectangles[i]) < minimum:
                min_index = i
                rectangles[j], rectangles[min_index] = rectangles[min_index], rectangles[j]

