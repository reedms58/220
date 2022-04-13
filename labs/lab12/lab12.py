"""
Name: Maddie Reed
lab12.py

Problem: This program creates a game where you guess numbers, edits lists, and checks inputs.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    if value in list:
        index = list.index(value)
        list.pop(index)
        name = "Maddie"
        list.insert(index, name)
    else:
        return None


def good_input():
    entered = 'n'
    good = 'y'
    while entered != good:
        num = eval(input('Enter a number: '))
        if num in range(1, 11):
            return num
        if num > 10:
            print("too high. enter a lower number.")
        if num < 1:
            print("too low. Enter a higher number.")


def num_digits():
    num = 1
    while num > 0:
        num = eval(input('Enter a number: '))
        if num <= 0:
            return None
        else:
            eval_num = num
            digits = 0
            while eval_num != 0:
                eval_num = eval_num // 10
                digits += 1
        print("your number has {} digit(s)".format(digits))


def hi_lo_game():
    secret_num = randint(1, 100)
    guesses = 7
    guess = 0
    while guesses != 0 and secret_num != guess:
        guess = eval(input("Enter a number between 1-100: "))
        guesses -= 1
        if guess == secret_num:
            num_guessed = 7 - guesses
            print("correct")
            print("You won in {} guesses!".format(num_guessed))
        if guess > secret_num:
            print("too high.")
        if guess < secret_num:
            print("too low.")
        if guesses == 0:
            print("you loose!")
            print("the number was {}".format(secret_num))
