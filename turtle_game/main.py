# Other functions
from art import text2art


# Colored text in console
def color_text():
    return print(f'\033[33;40m', end='')


color_text()


# Game selection and launch
def press_start():
    try:
        # Game selection
        game = input(
            '\tChoose a game:\n\t'
            'Turtle Racing - 1\n\t'
            'Catch the Cube - 2\n\t'
            'Painter - 3\n\t'
            'to exit write "exit"\n\t'
        )
        # The user entered an empty string
        if game == "":
            print('\n\tThe string cannot be empty')
            # Restart
            press_start()
        # Exiting the game
        elif game == 'exit':
            print('\n\tGoodbye!')
            return

        game = int(game)
        if game == 1:
            # Game title
            print(text2art(' T U R T L E     R A C I N G'))
            # My functions
            from turtle_racing.main_racing import start_main_racing
            # Launch the game
            start_main_racing()
        elif game == 2:
            # Game title
            print(text2art(' C A T C H     T H E     C U B E'))
            # My functions
            from catch_the_cube.main_cube import start_cube
            # Launch the game
            start_cube()
        elif game == 3:
            # Game title
            print(text2art(' P A I N T E R'))
            # My functions
            from painter.main_painter import start_painter
            # Launch the game
            start_painter()
        else:
            # Invalid input
            print('\n\tGame not found')
            # Restart
            press_start()
    # Error handling
    except ValueError:
        # The user entered not a number, but a letter
        print("\n\tEnter a number, not a letter")
        # Restart
        press_start()


# Main start
if __name__ == '__main__':
    # Start of the game
    press_start()