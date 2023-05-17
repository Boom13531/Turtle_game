import turtle

from turtle_game.turtle_racing.create_objects.turtle_players import colors
# Value for moving the turtle to the starting line
turtle_run = -475
# Create window and starting/finishing line
screen, pen_t = draw_screen()
# Rules and game information
information = ['Turtle Racing!',
               'You play as the yellow turtle.',
               'The goal of the game is to reach the finish line marked by a red line.',
               'You move by pressing keys on the keyboard.',
               'To win, press all the keys as quickly as possible!',
               'To start the game, click the mouse button.']

# Game information (printed on the game screen)
def info():
    # creature pen_info
    pen_info = turtle.Turtle()
    pen_info.hideturtle()
    pen_info.speed(0)
    pen_info.pensize(4)
    pen_info.penup()
    pen_info.goto(0, 200)
    # writes rules and information
    pen_info.write(f'{information[0]}', align="center", font=("Impact", 20, "normal"))
    pen_info.goto(0, 150)
    pen_info.color('yellow')
    pen_info.write(f'{information[1]}', align="center", font=("Comic Sans MS", 20, "normal"))
    pen_info.color('black')
    pen_info.goto(0, 100)
    pen_info.write(f'{information[2]}', align="center", font=("Comic Sans MS", 20, "normal"))
    pen_info.goto(0, 50)
    pen_info.write(f'{information[3]}', align="center", font=("Comic Sans MS", 20, "normal"))
    pen_info.goto(0, -0)
    pen_info.write(f'{information[4]}', align="center", font=("Georgia", 20, "normal"))
    pen_info.goto(0, -100)
    pen_info.write(f'{information[5]}', align="center", font=("Georgia", 20, "normal"))
    return pen_info


# Clear text and start main code
def clear_information(x, y):
    # Clear the text
    pen_info.clear()
    # Unbind the mouse click event handler
    screen.onclick(None)
    # Launch the game
    start_game(colors, turtle_run, screen, pen_t)