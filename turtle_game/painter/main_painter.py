import turtle
from turtle_game.painter.functions.keys import move_up, move_down, move_left, move_right
from turtle_game.painter.functions.keys import color_edit, pen_up_or_down, pen_fill, clear_screen
from turtle_game.painter.functions.keys import screen, pen, painter, move


def start_painter():
    def info():
        pen.write('''
                Изменить цвет - q
                Поднять/опустить перо - w
                Заливка - e
                Очистить экран - r
                Выход - p
                
                Чтобы начать игру, нажмите на кнопку мыши''',
                  align="center", font=("Comic Sans MS", 20, "normal"))

    def clear_info(x, y):
        pen.clear()
        screen.onclick(None)
        painter.showturtle()
        click_tracking()

    def click_tracking():
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_right, "Right")

        screen.onkey(color_edit, 'q')
        screen.onkey(pen_up_or_down, 'w')
        screen.onkey(pen_fill, 'e')
        screen.onkey(clear_screen, 'r')

        screen.onkey(exit, 'p')

        screen.onscreenclick(move)
        screen.listen()
        turtle.done()

    info()
    screen.onclick(clear_info)
    screen.listen()
    turtle.mainloop()


if __name__ == '__main__':
    start_painter()
