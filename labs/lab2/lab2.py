"""
Name: Maddie Reed
lab2.py

Problem: this program calculates the root square mean, the harmonic mean, geometric mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def means():
    rms_accumulator = 0
    hm_accumulator = 0
    gm_accumulator = 1
    number_of_values = eval(input("How many values are you entering? "))
    for i in range(number_of_values):
        values = eval(input("enter value: "))
        rms_accumulator = values ** 2 + rms_accumulator
        hm_accumulator = 1/values + hm_accumulator
        gm_accumulator = values * gm_accumulator
    root_mean_square = (rms_accumulator / number_of_values) ** (1 / 2)
    harmonic_mean = number_of_values / (1 / hm_accumulator)
    geometric_mean = gm_accumulator ** (1 / number_of_values)
    print("The square root mean is: ", round(root_mean_square, 3))
    print("The harmonic mean is: ", round(harmonic_mean, 3))
    print("The geometric mean is: ", round(geometric_mean, 3))
