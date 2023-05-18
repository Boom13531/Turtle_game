from turtle_game.painter.create.creating_screen import create

screen, painter, pen = create()
colors = ["red", "saddle brown", "yellow", "green", "dark slate blue", "purple", 'White', 'DarkOliveGreen']





def move(x, y):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()


def move_up():
    painter.setheading(90)
    painter.forward(10)


def move_down():
    painter.setheading(270)
    painter.forward(10)


def move_left():
    painter.setheading(180)
    painter.forward(10)


def move_right():
    painter.setheading(0)
    painter.forward(10)


def color_edit():
    painter.color(colors[pen.color_number])
    pen.color_number += 1
    len_color = len(colors)
    if pen.color_number == len_color:
        pen.color_number = 0


def pen_fill():
    if painter.fill == 'off':
        painter.begin_fill()
        painter.fill = 'on'
    elif painter.fill == 'on':
        painter.end_fill()
        painter.fill = 'off'


def pen_up_or_down():
    if painter.up_or_down == 'down':
        painter.penup()
        painter.up_or_down = 'up'
    elif painter.up_or_down == 'up':
        painter.pendown()
        painter.up_or_down = 'down'


def clear_screen():
    painter.clear()
