"""
Name: Maddie Reed
lab8.py

Problem: This program generates two randomly placed balls bouncing around a window.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time

from graphics import *
from random import randint


def get_random(move_amount):
    gen_num = randint(-move_amount, move_amount)
    return gen_num


def did_collide(ball1, ball2):
    rand_p1 = ball1.getCenter()
    rand_p1x = rand_p1.getX()
    rand_p1y = rand_p1.getY()
    rand_p2 = ball2.getCenter()
    rand_p2x = rand_p2.getX()
    rand_p2y = rand_p2.getY()
    rad1 = ball1.getRadius()
    rad2 = ball2.getRadius()

    distance = ((rand_p2x-rand_p1x)**2 + (rand_p2y-rand_p1y)**2)**(1/2)
    if distance <= rad1+rad2:
        return True
    else:
        return False


def hit_vertical(ball, win):
    rand_point = ball.getCenter()
    rand_point_y = rand_point.getY()
    rad = ball.getRadius()
    radius_y = rand_point_y + rad
    radius_neg_y = rand_point_y - rad
    if radius_y > win.getHeight():
        return True
    if radius_neg_y < 0:
        return True
    else:
        return False


def hit_horizontal(ball, win):
    rand_point = ball.getCenter()
    rand_point_x = rand_point.getX()
    rad = ball.getRadius()
    radius_x = rand_point_x + rad
    radius_neg_x = rand_point_x - rad
    if radius_x > win.getWidth():
        return True
    if radius_neg_x < 0:
        return True
    else:
        return False


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def bumper():
    width = 600
    height = 600
    win = GraphWin("Bumper Balls", width, height)

    point1x = randint(0, 600)
    point1y = randint(0, 600)
    point2x = randint(0, 600)
    point2y = randint(0, 600)
    rand_p1 = Point(point1x, point1y)
    rand_p2 = Point(point2x, point2y)
    ball1 = Circle(rand_p1, 30)
    ball2 = Circle(rand_p2, 30)
    color1 = get_random_color()
    color2 = get_random_color()
    ball1.setFill(color1)
    ball2.setFill(color2)
    ball1.draw(win)
    ball2.draw(win)

    ball1_move_x = get_random(20)
    ball1_move_y = get_random(20)
    ball2_move_x = get_random(20)
    ball2_move_y = get_random(20)

    while not win.checkMouse():
        if did_collide(ball1, ball2):
            ball1_move_x = - ball1_move_x
            ball1_move_y = - ball1_move_y
            ball2_move_x = - ball2_move_x
            ball2_move_y = - ball2_move_y
        if hit_vertical(ball1, win):
            ball1_move_y = - ball1_move_y
        if hit_vertical(ball2, win):
            ball2_move_y = - ball2_move_y
        if hit_horizontal(ball1, win):
            ball1_move_x = - ball1_move_x
        if hit_horizontal(ball2, win):
            ball2_move_x = - ball2_move_x
        time.sleep(0.1)
        ball1.move(ball1_move_x, ball1_move_y)
        ball2.move(ball2_move_x, ball2_move_y)

    win.close()


bumper()
