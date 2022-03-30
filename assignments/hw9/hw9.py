"""
Name: Maddie Reed
hw9.py

Problem: This program plays a game of hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import random


def get_words(file_name):
    my_file = open(file_name, 'r')
    words = []
    file_words = my_file.readlines()
    for word in file_words:
        word = word.replace('\n', '')
        words.append(word)
    return words


def get_random_word(words):
    num = random.randint(0, len(words))
    word = words[num]
    print(word)
    return word


def letter_in_secret_word(letter, secret_word):
    letter_num = secret_word.count(letter)
    if letter_num > 0:
        print("yes")
        return True
    else:
        print("no")
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    hidden_word = []
    for character in secret_word:
        if character in guesses:
            hidden_word.append(character)
        else:
            hidden_word.append("_")
    word = " ".join(hidden_word)
    return word


def won(guessed):
    if guessed.count("_") >= 0:
        return True
    else:
        return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    quessed = '_'
    while not won(guessed):
        print()


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
