# Other functions
import turtle


def create():
    # Creating window
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    turtle.screensize(canvwidth=400, canvheight=400,
                      bg="light steel blue")
    screen.title("Turtle painter")
    # Creating a player (painter)
    painter = turtle.Turtle()
    painter.hideturtle()
    painter.color('purple')
    painter.up_or_down = 'down'
    painter.fill = 'off'
    # Creating pen for write information
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-50, -100)
    pen.speed(0)
    pen.color('black')
    pen.color_number = 0

    return screen, painter, pen