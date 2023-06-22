# Other functions
import turtle
# My functions
from turtle_racing.create_objects.turtle_players import en1, en2, en3, en4, player



# Win animation
def victory_animation(t, pen_t, screen):
    # Hide the turtles
    def hide():
        en1.hideturtle()
        en2.hideturtle()
        en3.hideturtle()
        en4.hideturtle()
        player.hideturtle()

    hide()
    # Get the color of the turtle
    col_fill = t.color()[0]
    col = t.color()[-1]
    cornes_turtle = 270

    # Draw a circle with turtles
    class Drawing(turtle.Turtle):
        '''Circle'''

        def __init__(self, color, col_fill, cornes_turtle):
            super().__init__()
            self.hideturtle()
            self.speed(0)
            self.penup()
            self.shape('turtle')
            self.color(col_fill, color)
            self.setheading(cornes_turtle)
            self.fd(150)
            self.left(90)
            self.showturtle()

    # Circle made of turtles
    for i in range(24):
        turtle_circle = Drawing(col, col_fill, cornes_turtle)
        cornes_turtle += 15

    # Write 'Win'
    pen_t.pensize(10)
    pen_t.color(col)
    pen_t.goto(-20, 20)
    pen_t.write('Win', align="center", font=("Arial", 20, "normal"))
    pen_t.goto(40, 20)
    pen_t.write('!', align="center", font=("Arial", 20, "normal"))

    # Turtle in the center
    turtle_centre = Drawing(col, col_fill, 0)
    turtle_centre.goto(20, 35)

    # Star settings
    def star(x, y):
        star = turtle.Turtle()
        star.hideturtle()
        star.color('yellow')
        star.speed(0)
        star.penup()
        star.goto(x, y)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.forward(50)
            star.right(144)
        star.end_fill()

    # Star 1
    star(-85, 0)

    # Star 2
    star(-25, 0)

    # Star 3
    star(35, 0)

    # Сlick to exit
    turtle.exitonclick()