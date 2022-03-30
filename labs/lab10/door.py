"""
Name: Maddie Reed

door.py

Problem: Makes a Door class. Opens and closes when clicked

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Door:

    def __init__(self, shape, label, secret):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)
        self.secret = secret

    def get_label(self):
        label = self.text.getText()
        return label

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        clk_point_x = point.getX()
        clk_point_y = point.getY()
        point_1 = self.shape.getP1()
        point_2 = self.shape.getP2()
        point_1x = point_1.getX()
        point_1y = point_1.getY()
        point_2x = point_2.getX()
        point_2y = point_2.getY()
        if point_1x <= clk_point_x <= point_2x and point_1y <= clk_point_y <= point_2y:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret



