"""
Name: Maddie Reed
sphere.py

Problem: This class makes a sphere object.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


class Sphere:
    # constructor
    def __init__(self, radius):
        self.radius = radius

    # instance variables
    def get_radius(self):
        return self.radius

    # methods
    def surface_area(self):
        surf_area = 4 * math.pi * self.radius ** 2
        return surf_area

    def volume(self):
        vol = (4/3) * math.pi * self.radius ** 3
        return vol
