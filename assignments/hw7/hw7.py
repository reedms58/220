"""
Name: Maddie Reed
hw7.py

Problem: This program prints numbers and words from a file, calculates hourly wages
checks isbns, sends messages, and sends encoded messages.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import *


def number_words(in_file_name, out_file_name):
    read_file = open(in_file_name, "r")
    write_file = open(out_file_name, "w")
    in_string = read_file.read()
    file_list = in_string.split()
    acc = 0
    for word in file_list:
        acc = acc + 1
        output = str(acc) + word
        print(output, file=write_file)
    read_file.close()
    write_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    line_list = in_file.readlines()
    for line in line_list:
        worker = line.split()
        first_name = worker[0]
        last_name = worker[1]
        wage = worker[2]
        hours = worker[3]
        wage_bonus = eval(wage) + 1.65
        earned_cash = wage_bonus * eval(hours)
        print("{} {} ${:0<2}".format(first_name, last_name, earned_cash), file=out_file)
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    isbn_num = isbn.replace('-', '')
    acc = 0
    check_sum = 0
    for num in range(10, 1, -1):
        digit = eval(isbn_num[acc])
        acc = acc + 1
        check = digit * num
        check_sum = check_sum + check
    return check_sum


def send_message(file_name, friend_name):
    file = open(file_name, "r")
    friend = open(friend_name, "w")
    file_content = file.readlines()
    print(file_content, file=friend)
    file.close()
    friend.close()


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    friend = open(friend_name, "w")
    file_content = file.readlines()
    for line in file_content:
        encoded_mes = encode(line, key)
        print(encoded_mes, file=friend)
    file.close()
    friend.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, "r")
    friend = open(friend_name, "w")
    key_file = open(pad_file_name, "r")
    file_content = file.read()
    key_content = key_file.read()
    better_mes = encode_better(file_content, key_content)
    print(better_mes, file=friend)
    file.close()
    friend.close()
    key_file.close()


if __name__ == '__main__':
    pass
