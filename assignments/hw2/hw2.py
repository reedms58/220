"""
Name: Maddie Reed
hw2.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    sum= 0
    for i in range(3, upper_bound + 1, 3):
        sum = sum + i
    print("sum of threes is ", sum)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")


def triangle_area():
    pass


def sum_squares():
    pass


def power():
    pass


if __name__ == '__main__':
    pass
