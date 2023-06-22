# My functions
from painter.create.creating_screen import create

# Creating the screen, player, and pen
screen, painter, pen = create()

# Colors for drawing
colors = "red", "saddle brown", "yellow", "green", "dark slate blue", "purple", 'White', 'DarkOliveGreen'


# Move on mouse click
def move(x, y):
    # lift the pen up
    painter.penup()
    # Move the turtle graphics to the given coordinates
    painter.goto(x, y)
    # Put the pen down
    painter.pendown()


# Move up
def move_up():
    # Player direction - up
    painter.setheading(90)
    # Move the player
    painter.forward(10)


# Move down
def move_down():
    # Player direction - down
    painter.setheading(270)
    # Move the player
    painter.forward(10)


# Move left
def move_left():
    # Player direction - left
    painter.setheading(180)
    # Move the player
    painter.forward(10)


# Move right
def move_right():
    # Player direction - right
    painter.setheading(0)
    # Move the player
    painter.forward(10)


# Change pen color
def color_edit():
    # Choose the next color from the list
    painter.color(colors[pen.color_number])
    # Index color_number += 1
    pen.color_number += 1
    len_color = len(colors)
    # If the end of the list is reached - color_number equate 0
    if pen.color_number == len_color:
        pen.color_number = 0


# Fill shape
def pen_fill():
    # Check the fill status (off)
    if painter.fill == 'off':
        # Begin fill
        painter.begin_fill()
        # Fill status = on
        painter.fill = 'on'
    # Check the fill status (on)
    elif painter.fill == 'on':
        # End fill
        painter.end_fill()
        # Fill status = off
        painter.fill = 'off'


# Lift/drop pen
def pen_up_or_down():
    # Check the pen status (down)
    if painter.up_or_down == 'down':
        # Lift the pen
        painter.penup()
        # Pen status = up
        painter.up_or_down = 'up'
    # Check the pen status (up)
    elif painter.up_or_down == 'up':
        # Drop pen
        painter.pendown()
        # Pen status = down
        painter.up_or_down = 'down'


# Clear the screen
def clear_screen():
    # Clear the screen
    painter.clear()