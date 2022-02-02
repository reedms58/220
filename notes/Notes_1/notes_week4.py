# class is a way to organize objects
# objects are things like variables that store data

import math # this allows you to pull put functions from a stored library.


math.sqrt() # anything that is a <class>.<function> is a method
math.pi() # access with math.<function>

# constructor creates a object
# method is a function within a class

my_point = graphics.Point(50, 70)
point_a = graphics.Point(70, 90)
print(point_a.getX(), point_a.getY())
point_a.move(10, 0)
print(point_a.getX(), point_a.getY())

win = graphics.GraphWin("title", 700, 700) # the numbers in the window is the graph's dimentions
middle = graphics.Point(350, 350)
middle.draw(win)
input('hit enter to close')

# when importing classes you can also say: you no longer have to say <class.func>
from graphics import Point, GraphWin, Circle

my_circle = Circle(middle, 40)
my_circle.draw(win)

# making a face
win = GraphWin("Face", 700, 700)
face = Circle((350, 100), 100)
face.draw(win)

left_eye = Circle(Point(320, 60), 15)
right_eye = Circle(Point(380, 60), 15)
# you can also use the command <variable>.clone()


left_eye.setFill('yellow')
left_eye.setOutline('green')
right_eye.setFill('yellow')
right_eye.setOutline('green')

left_eye.draw(win)
right_eye.draw(win)
input("hit enter to close")

for i in range(100):
    click_point = win.getMouse()  # this waits for a click on the screen
    print(click_point.getX(), click_point.getY())
    click_point.draw(win)
win.getMouse()
