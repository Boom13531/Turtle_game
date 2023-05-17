import turtle

def start_paint():
    colors = ["red", "saddle brown", "yellow", "green", "dark slate blue", "purple", 'White', 'DarkOliveGreen']
    scr = turtle.Screen()
    scr.setup(width=600, height=600)
    turtle.screensize(canvwidth=400, canvheight=400,
                      bg="light steel blue")
    scr.title("Черепашья графика")
    t = turtle.Turtle()
    t.color('purple')
    t.pd = 'down'
    t.fi = 'off'

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 100)
    pen.speed(0)
    pen.color('black')
    pen.write('''
    Изменить цвет - q
    Поднять/опустить перо - w
    Заливка - e
    Очистить экран - r
    Выход - p''', align="center", font=("Arial", 30, "normal"))
    pen.cl = 0
    pen.color_number = 0
    def draw(x, y):
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        t.goto(x, y)

    def move(x, y):
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1

        t.penup()

        t.goto(x, y)

        t.pendown()

        t.ondrag(draw)


    def move_up():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        t.setheading(90)
        t.forward(10)

    def move_down():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        t.setheading(270)
        t.forward(10)

    def move_left():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        t.setheading(180)
        t.forward(10)

    def move_right():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        t.setheading(0)
        t.forward(10)

    def col():
        def color_edit(colors):
            if pen.cl == 0:
                pen.clear()
                pen.cl = 1
            t.color(colors[pen.color_number])
            pen.color_number +=1
            l = len(colors)
            if pen.color_number == l:
                pen.color_number = 0
        color_edit(colors)

    def pen_fill():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        if t.fi == 'off':
            t.begin_fill()
            t.fi = 'on'
        elif t.fi == 'on':
            t.end_fill()
            t.fi = 'off'

    def pen_up_or_down():
        if pen.cl == 0:
            pen.clear()
            pen.cl = 1
        if t.pd == 'down':
            t.penup()
            t.pd = 'up'
        elif t.pd == 'up':
            t.pendown()
            t.pd = 'down'
    def clear_screen():
        t.clear()
    def exit(): scr.bye()


    scr.onkeypress(move_up, "Up")
    scr.onkeypress(move_down, "Down")
    scr.onkeypress(move_left, "Left")
    scr.onkeypress(move_right, "Right")
    scr.onkey(col, 'q')
    scr.onkey(pen_up_or_down, 'w')
    scr.onkey(pen_fill, 'e')
    scr.onkey(clear_screen, 'r')
    scr.onkey(exit, 'p')


    scr.onscreenclick(move)

    scr.listen()
    turtle.done()
if __name__ == '__main__':
    start_paint()