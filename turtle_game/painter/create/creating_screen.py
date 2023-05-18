import turtle
def create():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    turtle.screensize(canvwidth=400, canvheight=400,
                      bg="light steel blue")
    screen.title("Черепашья графика")
    painter = turtle.Turtle()
    painter.hideturtle()
    painter.color('purple')
    painter.up_or_down = 'down'
    painter.fill = 'off'

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, -50)
    pen.speed(0)
    pen.color('black')
    pen.color_number = 0
    return screen, painter, pen

