#My functions
from turtle_game.catch_the_cube.function.function import \
    draw_screen,\
    create_cube,\
    respawn_cube,\
    move_cubes

def start_cube():

    screen, pen_score = draw_screen()

    # функция клика на кубик
    def click(x, y):
        respawn_cube(x, y, cubes, pen_score, screen)

    # обработчик кликов мыши
    screen.onclick(click)

    # вызываем функцию создания кубика
    cubes = create_cube()

    # вызываем функцию движения кубиков
    move_cubes(cubes, pen_score, screen)

# Start of the code
if __name__ == '__main__':
    start_cube()