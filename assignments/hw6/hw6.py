"""
Name: Maddie Reed
hw6.py

Problem: This program turns ints and floats into cash, encodes a message
calculates the area and volume of a sphere, calculates the sum natural
numbers and cubed natural numbers, and encodes a message better.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from math import pi


def cash_converter():
    integer = eval(input("enter an integer: "))
    num_float = float(integer)
    num_string = str(num_float)
    num_list = num_string.split('.')
    dollar = num_list[0]
    cents = num_list[1]
    output = "That is ${}.{:0<2}".format(dollar, cents)
    print(output)


def encode():
    ordinals = []
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for character in message:
        num = ord(character)
        shift = num + key
        new_num = chr(shift)
        ordinals.append(new_num)
    output = "".join(ordinals)
    print(output)


def sphere_area(radius):
    area = float(4) * float(radius**2) * pi
    return area


def sphere_volume(radius):
    volume = float(4/3) * pi * radius ** 3
    return volume


def sum_n(number):
    total = 0
    for num in range(1, number + 1):
        total = num + total
    return total


def sum_n_cubes(number):
    total = 0
    for num in range(1, number + 1):
        total = num**3 + total
    return total


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    key_len = len(key)
    length = len(message)
    encoded_mess = ''
    for i in range(length):
        shift = ord(key[i % key_len]) - 65
        num = ord(message[i]) - 65
        new_num = (num + shift) % 58
        characters = chr(new_num + 65)
        encoded_mess = encoded_mess + characters
    print(encoded_mess)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
