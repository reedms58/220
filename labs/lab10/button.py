"""
Name: Maddie Reed
button.py

Problem: Makes a Button class. Does an action when clicked.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)

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
        click_x = point.getX()
        click_y = point.getY()
        sha_point_1 = self.shape.getP1()
        sha_point_2 = self.shape.getP2()
        sha_point_1x = sha_point_1.getX()
        sha_point_1y = sha_point_1.getY()
        sha_point_2x = sha_point_2.getX()
        sha_point_2y = sha_point_2.getY()
        if sha_point_1x <= click_x <= sha_point_2x and sha_point_1y <= click_y <= sha_point_2y:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
