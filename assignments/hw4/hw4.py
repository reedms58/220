"""
Name: <Maddie Reed>
hw4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can add square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(0, 0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to add square
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()
        # clone square for each click
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        added_square = shape.clone()
        added_square.move(change_x, change_y)
        added_square.draw(win)

    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click twice to make a rectangle")
    instructions.draw(win)

    click_1 = win.getMouse()
    click_2 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())
    point_2 = Point(click_2.getX(), click_2.getY())
    rec = Rectangle(point_1, point_2)
    rec.setFill('green')
    rec.draw(win)

    side_1 = click_2.getX() - click_1.getX()
    side_2 = click_2.getY() - click_1.getX()
    calc_perimeter = abs(side_1 * 2) + abs(side_2 * 2)
    calc_area = abs(side_1 * side_2)

    peri_string = "Perimeter: ", str(calc_perimeter)
    area_string = "Area: ", str(calc_area)
    perimeter = Text(Point(200, 350), peri_string)
    area = Text(Point(200, 370), area_string)
    perimeter.draw(win)
    area.draw(win)

    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click twice to make a circle")
    instructions.draw(win)

    click_1 = win.getMouse()
    click_2 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())
    circum_1 = click_2.getX() - click_1.getX()
    circum_2 = click_2.getY() - click_1.getY()
    distance = (circum_1 ** 2 + circum_2 ** 2) ** (1/2)
    circ = Circle(point_1, distance)
    circ.setFill('light blue')
    circ.draw(win)

    radius_string = "Radius: ", distance
    radius = Text(Point(200, 370), radius_string)
    radius.draw(win)

    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()


def pi2():
    terms = eval(input("enter the number of terms to sum: "))
    accumulator = 0
    for i in range(1, terms + 1, 2):
        accumulator = accumulator + 4/i - 4/(i+2)
    print("pi approximation: ", accumulator)
    accuracy = abs(math.pi - accumulator)
    print("accuracy: ", accuracy)

pi2()


if __name__ == '__main__':
    pass
