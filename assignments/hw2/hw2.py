"""
Name: Maddie Reed
hw2.py

Problem: This program calculates the sum of threes, the area of a triangle, the sum of
squares, exponents, and makes a multiplication table.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    total = 0
    for i in range(3, upper_bound + 1, 3):
        total = total + i
    print("sum of threes is ", total)


def multiplication_table():
    for i in range(1, 11):
        print('\n')
        for j in range(1, 11):
            print(i * j, end='\t')


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    semi_p = (side_a + side_b + side_c) / 2
    area = math.sqrt((semi_p*(semi_p-side_a)*(semi_p-side_b)*(semi_p-side_c)))
    print("Area is ", area)


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    total = 0
    for i in range(lower_range, upper_range + 1):
        total = (i * i) + total
    print(total)


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    answer = 1
    for i in range(exponent):
        answer = base * answer
    print(base, "^", exponent, "=", answer)


if __name__ == '__main__':
    pass
