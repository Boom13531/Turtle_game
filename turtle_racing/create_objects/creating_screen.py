import turtle


def draw_screen():
    # Window
    screen = turtle.Screen()
    screen.score = 0
    screen.title("Turtle Racing")
    screen.bgcolor("white")
    screen.setup(width=1000, height=600)
    turtle.screensize(canvwidth=400, canvheight=400, bg="light steel blue")

    # Pen for drawing lines
    pen_t = turtle.Turtle()
    pen_t.hideturtle()
    pen_t.speed(0)
    pen_t.pensize(4)
    pen_t.penup()
    pen_t.color("red")
    pen_t.goto(450, 300)
    pen_t.right(90)
    pen_t.pendown()
    pen_t.fd(600)
    pen_t.goto(-450, -300)
    pen_t.left(180)
    pen_t.fd(600)
    pen_t.right(90)
    pen_t.fd(900)
    pen_t.penup()

    return screen, pen_t