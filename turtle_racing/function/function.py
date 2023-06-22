# My functions
from turtle_racing.function.victory import victory_animation
from turtle_racing.create_objects.turtle_players import *


def start_game(colors, turtle_run, screen, pen_t):



    # Functions for moving the player turtle - tap_key() is for mouse click and tap() is for keyboard press
    def tap_key(x, y):
        player.fd(20)

    def tap():
        player.fd(5)

    # The finish line
    finish = 440

    # Mouse click event listener on the player turtle
    player.onclick(tap_key)

    # Keyboard event listener for tapping (moving) the player turtle
    screen.onkey(tap, "")

    # Waiting for mouse clicks and key presses
    screen.listen()

    # Turtles movement
    while en1.xcor() < finish and\
            en2.xcor() < finish and\
            en3.xcor() < finish and\
            en4.xcor() < finish and\
            player.xcor() < finish:
        for participant in participants:
            participant.run()


    # Summarize the result
    max_x = max(en1.xcor(), en2.xcor(), en3.xcor(), en4.xcor(), player.xcor())

    if player.xcor() == max_x:
        victory_animation(player, pen_t, screen)
    if en1.xcor() == max_x:
        victory_animation(en1, pen_t, screen)
    if en2.xcor() == max_x:
        victory_animation(en2, pen_t, screen)
    if en3.xcor() == max_x:
        victory_animation(en3, pen_t, screen)
    if en4.xcor() == max_x:
        victory_animation(en4, pen_t, screen)
if __name__ == '__main__':
    start_game()