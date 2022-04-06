"""
Name: Maddie Reed
lab11.py

Problem: This program creates a game with three doors. The user can guess which door
is a secret door.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def three_door_game():
    win = GraphWin("Three Door Game", 800, 800)

    rec_1 = Rectangle(Point(30, 230), Point(230, 615))
    rec_2 = Rectangle(Point(300, 230), Point(500, 615))
    rec_3 = Rectangle(Point(570, 230), Point(770, 615))
    wins_rec = Rectangle(Point(30, 40), Point(100, 110))
    loss_rec = Rectangle(Point(100, 40), Point(170, 110))
    butt_rec = Rectangle(Point(570, 40), Point(770, 110))

    num_wins = 0
    num_loss = 0

    directions = Text(Point(400, 710), "Click to guess which is the secret door")
    result_txt = Text(Point(400, 160), "I have a secret door")
    wins_num_txt = Text(wins_rec.getCenter(), num_wins)
    loss_num_txt = Text(loss_rec.getCenter(), num_loss)
    wins_txt = Text(Point(65, 33), "wins")
    loss_txt = Text(Point(135, 33), "looses")

    secret = False

    door_1 = Door(rec_1, "Door 1", secret)
    door_2 = Door(rec_2, "Door 2", secret)
    door_3 = Door(rec_3, "Door 3", secret)
    quit_button = Button(butt_rec, "Quit")

    door_1.color_door("saddle brown")
    door_2.color_door("saddle brown")
    door_3.color_door("saddle brown")

    directions.draw(win)
    result_txt.draw(win)
    wins_rec.draw(win)
    loss_rec.draw(win)
    wins_num_txt.draw(win)
    loss_num_txt.draw(win)
    wins_txt.draw(win)
    loss_txt.draw(win)

    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    quit_button.draw(win)

    door_list = [door_1, door_2, door_3]

    click = win.getMouse()
    while not quit_button.is_clicked(click):
        secret_num = randint(1, 3)
        secret_door = door_list.pop(secret_num - 1)
        secret_door.set_secret(True)

        if secret_door.is_clicked(click):
            secret_door.color_door("green")
            result_txt.setText("you win!")
            num_wins += 1
            wins_num_txt.setText(num_wins)
            directions.setText("Click anywhere to play again")
        elif door_list[0].is_clicked(click):
            door_list[0].color_door("red")
            result_txt.setText("incorrect!")
            num_loss += 1
            loss_num_txt.setText(num_loss)
            directions.setText("Click anywhere to play again")
        elif door_list[1].is_clicked(click):
            door_list[1].color_door("red")
            result_txt.setText("incorrect!")
            num_loss += 1
            loss_num_txt.setText(num_loss)
            directions.setText("Click anywhere to play again")

        click = win.getMouse()
        if quit_button.is_clicked(click):
            break

        door_list = [door_1, door_2, door_3]
        for door in door_list:
            door.color_door("saddle brown")
        directions.setText("Click to guess which is the secret door")
        result_txt.setText("I have a secret door")

        click = win.getMouse()

    win.close()
