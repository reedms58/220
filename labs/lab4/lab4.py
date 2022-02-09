"""
Name: Maddie Reed
lab2.py

Problem: Makes an animated Valentine's Day greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def greeting_card():
    width = 400
    height = 400
    win = GraphWin("Valentine's Day Message", width, height)

    left_circle = Circle(Point(170, 110), 60)
    left_circle.setFill('pink')
    left_circle.setOutline('pink')
    left_circle.draw(win)

    right_circle = left_circle.clone()
    right_circle.move(80, 0)
    right_circle.draw(win)

    point_1 = Point(123, 147)
    point_2 = Point(210, 228)
    point_3 = Point(298, 147)
    triangle = Polygon(point_1, point_2, point_3)
    triangle.setFill('pink')
    triangle.setOutline('pink')
    triangle.draw(win)

    message = Text(Point(210, 135), "A + M")
    message.setSize(25)
    message.draw(win)

    point_4 = Point(0, 380)
    point_5 = Point(120, 210)
    arrow = Line(point_4, point_5)
    arrow.setArrow("last")
    arrow.draw(win)

    for i in range(8):
        arrow.undraw()
        arrow.move(21, -21)
        arrow.draw(win)
        time.sleep(0.1)

    close = Text(Point(200, 350), "Click again to close")
    close.draw(win)

    win.getMouse()


greeting_card()
