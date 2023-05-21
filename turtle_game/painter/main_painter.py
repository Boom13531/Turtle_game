# Other functions
import turtle
# My functions
from turtle_game.painter.functions.keys import move_up, move_down, move_left, move_right
from turtle_game.painter.functions.keys import color_edit, pen_up_or_down, pen_fill, clear_screen
from turtle_game.painter.functions.keys import screen, pen, painter, move


# Game start function
def start_painter():
    # Write information
    def info():
        pen.write('''
        Change color - q
        Raise/lower pen - w
        Fill - e
        Clear screen - r
        Output - p
        
        To start the game,
        click on the mouse button''',
                  align="center", font=("Comic Sans MS", 20, "normal"))
    # Clear information (cleared after clicking the mouse button)
    def clear_info(x, y):
        # Clear info
        pen.clear()
        # Disabling click tracking
        screen.onclick(None)
        # Show painter
        painter.showturtle()

        # Launches click_tracking
        click_tracking()

    def click_tracking():
        # Tracking move (keys)
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_right, "Right")

        # Tracking key
        screen.onkey(color_edit, 'q')
        screen.onkey(pen_up_or_down, 'w')
        screen.onkey(pen_fill, 'e')
        screen.onkey(clear_screen, 'r')
        screen.onkey(exit, 'p')

        # Tracking move (mouse)
        screen.onscreenclick(move)
        screen.listen()
        turtle.done()


    info()
    screen.onclick(clear_info)
    screen.listen()
    turtle.mainloop()

# Start of the code
if __name__ == '__main__':
    start_painter()