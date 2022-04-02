"""
Name: Maddie Reed
hw9.py

Problem: This program plays a game of hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import random
from graphics import *


def get_words(file_name):
    my_file = open(file_name, 'r')
    words = []
    file_words = my_file.readlines()
    for word in file_words:
        words.append(word)
    return words


def get_random_word(words):
    num = random.randint(0, len(words)-1)
    word = words[num]
    word = word.replace('\n', '')
    print(word)
    return word


def letter_in_secret_word(letter, secret_word):
    letter_num = secret_word.count(letter)
    if letter_num > 0:
        return True
    else:
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
    if guessed.count("_") <= 0:
        return True
    else:
        return False


def play_graphics(secret_word):
    win = GraphWin("Hangman", 500, 700)
    guessed = []

    head = Circle(Point(200, 145), 20)
    body = Line(Point(200, 165), Point(200, 365))
    r_leg = Line(Point(200, 365), Point(250, 500))
    l_leg = Line(Point(200, 365), Point(150, 500))
    r_arm = Line(Point(200, 200), Point(250, 275))
    l_arm = Line(Point(200, 200), Point(150, 275))

    man = [head, body, r_leg, l_leg, r_arm, l_arm]

    foot = Line(Point(150, 550), Point(350, 550))
    pole = Line(Point(300, 550), Point(300, 100))
    top = Line(Point(300, 100), Point(200, 100))
    rope = Line(Point(200, 100), Point(200, 125))
    foot.draw(win)
    pole.draw(win)
    top.draw(win)
    rope.draw(win)
    prompt = Text(Point(75, 680), "Guess a letter:")
    prompt.draw(win)

    guessed_txt = Text(Point(450, 250), guessed)
    guessed_txt.draw(win)

    num_guess = 6
    num_guessed = 0
    word_prog = make_hidden_secret(secret_word, guessed)
    while num_guess > 0 and not won(word_prog):
        num_guess = 6 - num_guessed

        secret_prog = Text(Point(250, 630), word_prog)
        secret_prog.draw(win)

        enter_let = Entry(Point(250, 680), 3)
        enter_let.draw(win)
        win.getMouse()
        letter = enter_let.getText()
        guessed = guessed + [letter]
        guess_len = len(guessed)
        guessed_txt.setText(guessed[0:guess_len])

        word_prog = make_hidden_secret(secret_word, guessed)
        if not letter_in_secret_word(letter, secret_word):
            man[num_guessed].draw(win)
            num_guessed = num_guessed + 1

    if won(word_prog):
        winner = Text(Point(250, 50), "winner!")
        winner.draw(win)

    else:
        loser = Text(Point(250, 50), "you loose!"+" the word was {}".format(secret_word))
        loser.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed = []
    num_guess = 6
    num_guessed = 0
    word_prog = make_hidden_secret(secret_word, guessed)
    while num_guess > 0 and not won(word_prog):
        num_guess = 6 - num_guessed
        print(guessed)
        print("guesses remaining: ", num_guess)
        print(word_prog)
        letter = input("guess a letter: ")
        guessed = guessed + [letter]
        word_prog = make_hidden_secret(secret_word, guessed)
        if not letter_in_secret_word(letter, secret_word):
            num_guessed = num_guessed + 1
    if won(word_prog):
        print("winner!")
        print("the word is:", secret_word)
    else:
        print("you loose!")
        print("the word was:", secret_word)


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
