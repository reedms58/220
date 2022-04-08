"""
Name: Maddie Reed
face.py

Problem: A class that makes a Face in a graphics window.
Face can express a smile, wink, and shocked expression.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0

        self.size = size
        self.window = window
        self.center = center

        self.head = Circle(center, size)
        self.head.draw(window)

        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)

        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_size = 0.8 * self.size
        mouth_off = self.size / 2.0
        point_1 = self.center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = self.center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        point_3 = self.center.clone()
        point_3.move(0, self.size / 1.5)
        self.mouth.undraw()
        self.mouth = Polygon(point_1, point_2, point_3)
        self.mouth.draw(self.window)

    def shock(self):
        mouth_size = 0.15 * self.size
        point_1 = self.center.clone()
        point_1.move(0, self.size/2.0)
        self.mouth.undraw()
        self.mouth = Circle(point_1, mouth_size)
        self.mouth.draw(self.window)

    def wink(self):
        eye_off = self.size / 3.0
        point_1 = self.center.clone()
        point_1.move(-eye_off + eye_off/2, -eye_off)
        point_2 = self.center.clone()
        point_2.move(-eye_off - eye_off/2, -eye_off)
        self.left_eye.undraw()
        self.left_eye = Line(point_1, point_2)
        self.left_eye.draw(self.window)
        self.smile()
