# My functions
from turtle_game.catch_the_cube.function.function import \
    draw_screen, \
    create_cube, \
    respawn_cube, \
    move_cubes


# Game start function
def start_cube():
    screen, pen_score = draw_screen()

    # function for clicking on the cube
    def click(x, y):
        respawn_cube(x, y, cubes, pen_score, screen)

    # mouse click handler
    screen.onclick(click)

    # call the function to create the cube
    cubes = create_cube()

    # call the function to move the cubes
    move_cubes(cubes, pen_score, screen)


# Start of the code
if __name__ == '__main__':
    start_cube()