"""
Name: Maddie Reed
lab10.py

Problem: Creates a door that alternated between closed and open based on user's clicks.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from door import *
from button import *


def main():
    win = GraphWin("lab 10", 500, 700)

    d_p1, d_p2 = Point(100, 100), Point(400, 600)
    d_shape = Rectangle(d_p1, d_p2)
    door = Door(d_shape, "Closed", True)

    b_p1, b_p2 = Point(100, 10), Point(400, 90)
    b_shape = Rectangle(b_p1, b_p2)
    button = Button(b_shape, "Exit")

    door.color_door('red')
    door.draw(win)
    button.draw(win)

    click = win.getMouse()
    while not button.is_clicked(click):
        if door.is_clicked(click):
            if door.get_label() == "Closed":
                door.open('white', 'Open')
            else:
                door.close('red', 'Closed')
        click = win.getMouse()

    win.close()


main()


