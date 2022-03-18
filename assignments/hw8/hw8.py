"""
Name: Maddie Reed
hw8.py

Problem: This program calculates the sum of squares in a list, evaluates if a wrestler can be a
starter, if it's a leap year, and if circles overlap.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import sqrt

from graphics import GraphWin, Circle


def add_ten(nums):
    len_nums = len(nums)
    for element in range(len_nums):
        new_nums = nums[element] + 10
        nums[element] = new_nums


def square_each(nums):
    list_len = len(nums)
    for element in range(list_len):
        new_nums = nums[element] * nums[element]
        nums[element] = new_nums
    return nums


def sum_list(nums):
    list_len = len(nums)
    total = 0
    for element in range(list_len):
        total = total + nums[element]
    return float(total)


def to_numbers(nums):
    list_len = len(nums)
    for element in range(list_len):
        flo_nums = float(nums[element])
        nums[element] = flo_nums


def sum_of_squares(nums):
    nums_length = len(nums)
    for element in range(nums_length):
        inside_list = nums[element].split(',')
        list_len = len(inside_list)
        for num in range(list_len):
            flo_nums = float(inside_list[num])
            inside_list[num] = flo_nums
        squared_list = square_each(inside_list)
        sum_nums = sum_list(squared_list)
        nums[element] = sum_nums
    return nums


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and not year % 100 == 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    x_calc = (center_2.getX() - circumference_point_2.getX())
    radius_2 = sqrt(
         x_calc ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    center_one = circle_one.getCenter()
    p1x = center_one.getX()
    p1y = center_one.getY()
    center_two = circle_two.getCenter()
    p2x = center_two.getX()
    p2y = center_two.getY()
    rad1 = circle_one.getRadius()
    rad2 = circle_two.getRadius()

    distance = ((p2x - p1x) ** 2 + (p2y - p1y) ** 2) ** (1 / 2)
    if distance <= rad1 + rad2:
        print("The circles overlap.")
        return True
    else:
        print("The circles do not overlap.")
        return False


if __name__ == '__main__':
    pass
