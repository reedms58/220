"""
Name: Maddie Reed
lab5.py

Problem: This program displays a triangle created by the user, and
calculates the perimeter and area. Displays color entered by user,
processes strings and lists, evaluates a series and makes a target.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from hw8.graphics import *


def triangle():
    width = 400
    height = 400
    win = GraphWin("Triangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click three times to make a triangle")
    instructions.draw(win)

    click_1 = win.getMouse()
    click_2 = win.getMouse()
    click_3 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())
    point_2 = Point(click_2.getX(), click_2.getY())
    point_3 = Point(click_3.getX(), click_3.getY())
    tri = Polygon(point_1, point_2, point_3)
    tri.setFill('light blue')
    tri.draw(win)

    side_1dx = (click_1.getX() - click_2.getX()) ** 2
    side_1dy = (click_1.getY() - click_2.getY()) ** 2
    length_1 = (side_1dx + side_1dy) ** (1/2)
    side_2dx = (click_2.getX() - click_3.getX()) ** 2
    side_2dy = (click_2.getY() - click_3.getY()) ** 2
    length_2 = (side_2dx + side_2dy) ** (1/2)
    side_3dx = (click_3.getX() - click_1.getX()) ** 2
    side_3dy = (click_3.getY() - click_1.getY()) ** 2
    length_3 = (side_3dx + side_3dy) ** (1/2)
    calc_perimeter = length_1 + length_2 + length_3

    semi = calc_perimeter / 2
    calc_area = (semi*(semi-length_1)*(semi-length_2)*(semi-length_3))**(1/2)

    peri_string = "Perimeter: " + str(calc_perimeter)
    area_string = "Area: " + str(calc_area)
    perimeter = Text(Point(200, 350), peri_string)
    area = Text(Point(200, 370), area_string)
    perimeter.draw(win)
    area.draw(win)

    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry_pt = Point(win_width / 2 + 15, win_height / 2 + 40)
    red_entry = Entry(red_entry_pt, 7)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry_pt = red_entry_pt.clone()
    green_entry_pt.move(0, 30)
    green_entry = Entry(green_entry_pt, 7)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry_pt = red_entry_pt.clone()
    blue_entry_pt.move(0, 60)
    blue_entry = Entry(blue_entry_pt, 7)

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    # display rgb text

    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    win.getMouse()
    win.close()

    for i in range(5):
        red = eval(red_entry.getText())
        green = eval(green_entry.getText())
        blue = eval(blue_entry.getText())
        shape.setFill(color_rgb(red, green, blue))
        win.getMouse()

    # Wait for another click to exit
    close = Text(Point(200, 200), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def process_string():
    string = input("Enter a word: ")
    # 1
    ans1 = string[0]
    print(ans1)
    # 2
    len_of_str = len(string)
    ans2 = string[len_of_str-1]
    print(ans2)
    # 3
    ans3 = string[1:5]
    print(ans3)
    # 4
    ans4 = ans1 + ans2
    print(ans4)
    # 5
    ans5 = string[0:3] * 10
    print(ans5)
    # 6
    for letter in string:
        print(letter)
    # 7
    print(len_of_str)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    # 1
    x = values[1] + values[3]
    print(x)
    # 2
    x = values[0] + values[2]
    print(x)
    # 3
    x = values[1] * 5
    print(x)
    # 4
    x = values[2:5]
    print(x)
    # 5
    x = values[2:4]
    x = x + [values[0]]
    print(x)
    # 6
    x = [values[2]] + [values[0]] + [float(values[5])]
    print(x)
    # 7
    x = values[2] + values[0] + float(values[5])
    print(x)
    # 8
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter the number of terms: "))
    values = [2, 4, 6]
    total = 0
    for i in range(terms):
        series = values[i % 3]
        total = total + series
        print(series, end=' ')
    print(end='\n')
    print("sum = ", total)


def target():
    width = 400
    height = 400
    win = GraphWin("Target", width, height)

    color_list = ['white', 'black', 'blue', 'red', 'yellow']
    win.setBackground('black')

    for i in range(5):
        center_pt = Point(width/2, height/2)
        radius = 200 - i * 40
        circle = Circle(center_pt, radius)
        circle.setFill(color_list[i])
        circle.draw(win)

    win.getMouse()
    win.close()
