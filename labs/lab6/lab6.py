"""
Name: Maddie Reed
lab6.py

Problem: This program uses the vigenere cipher to encode a message.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def vigenere_cipher():
    width = 600
    height = 400
    win = GraphWin("Vigenere", width, height)

    instr = Text(Point(80, 50), "Message to code")
    key_prompt = Text(Point(80, 100), "Enter Keyword")
    instr.draw(win)
    key_prompt.draw(win)

    enter_message = Entry(Point(350, 50), 30)
    enter_key = Entry(Point(350, 100), 30)
    enter_message.draw(win)
    enter_key.draw(win)

    encode_button = Rectangle(Point(275, 150), Point(375, 200))
    encode_button.draw(win)
    button_center = encode_button.getCenter()
    encode = Text(button_center, "Encode")
    encode.draw(win)

    win.getMouse()
    message = enter_message.getText()
    cap_message = message.upper()
    striped_message = cap_message.replace(" ", "")
    key = enter_key.getText()

    fixed_key = key.upper()
    key_len = len(fixed_key)
    length = len(striped_message)
    encoded_mess = ''
    for i in range(length):
        shift = ord(fixed_key[i % key_len]) - 65
        num = ord(striped_message[i]) - 65
        new_num = (num + shift) % 26
        characters = chr(new_num + 65)
        encoded_mess = encoded_mess + characters

    encode.undraw()
    encode_button.undraw()
    result_prompt = Text(Point(325, 225), "Resulting Message")
    text_mess = Text(Point(325, 250), encoded_mess)
    text_mess.draw(win)
    result_prompt.draw(win)

    close = Text(Point(300, 380), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()
