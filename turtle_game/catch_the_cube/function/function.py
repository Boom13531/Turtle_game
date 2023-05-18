# Other functions
import turtle, random
#My functions
from сatch_the_cube.function.cubes import Cubes

def draw_screen():
    # создаем окно
    screen = turtle.Screen()
    screen.score = 0
    screen.title("Поймай кубик")
    screen.bgcolor("white")
    screen.setup(width=600, height=730, starty=0)
    turtle.screensize(canvwidth=400, canvheight=400,
                      bg="black")


    field1 = turtle.Turtle()
    field1.speed(0)
    field1.color("white")
    field1.pensize(5)
    field1.hideturtle()
    field1.penup()
    field1.goto(-250, -150)
    field1.pendown()
    for i in range(4):
        field1.fd(500)
        field1.left(90)

    pen_score = turtle.Turtle()
    pen_score.speed(0)
    pen_score.penup()
    pen_score.hideturtle()
    pen_score.color("white")
    pen_score.goto(-250, -200)
    pen_score.pendown()
    pen_score.write("Счёт: {}".format(screen.score), align="left", font=("Arial", 30, "normal"))
    pen_score.penup()

    return screen, pen_score

# функция создания кубика
def create_cube():
    cube1 = Cubes()
    cube2 = Cubes()
    # создаем список кубиков
    cubes = []
    cubes.append(cube1)
    cubes.append(cube2)
    return cubes


def respawn_cube(x, y, cubes, pen_score, screen):
    for cube in cubes:
        if cube.distance(x, y) < 20:
            # добавление очков
            screen.score += 1
            cube.speed(0)
            cube.setposition(random.randint(-240, 240), random.randint(250, 340))
            cube.speed(random.randint(4, 7))
            pen_score.clear()
            pen_score.goto(-250, -200)
            pen_score.write("Счёт: {}".format(screen.score), align="left", font=("Arial", 30, "normal"))
            pen_score.penup()

# движение кубиков
def move_cubes(cubes, pen_score, screen):
    try:
        for cube in cubes:
            cube.run(pen_score, screen)
        move_cubes(cubes, pen_score, screen)
    except:
        pass