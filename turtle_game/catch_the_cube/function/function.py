# Other functions
import turtle, random

#My functions
from turtle_game.catch_the_cube.function.cubes import Cubes

def draw_screen():
    # создаём окно
    screen = turtle.Screen()
    screen.score = 0
    screen.title("Catch The Cube")
    screen.bgcolor("white")
    screen.setup(width=600, height=730, starty=0)
    turtle.screensize(canvwidth=400, canvheight=400,
                      bg="black")

    # Creating field
    field = turtle.Turtle()
    field.speed(0)
    field.color("white")
    field.pensize(5)
    field.hideturtle()
    field.penup()
    field.goto(-250, -150)
    field.pendown()
    for i in range(4):
        field.fd(500)
        field.left(90)

    # Creating score pen
    pen_score = turtle.Turtle()
    pen_score.speed(0)
    pen_score.penup()
    pen_score.hideturtle()
    pen_score.color("white")
    pen_score.goto(-250, -200)
    pen_score.pendown()
    pen_score.write(f"Score: {screen.score}",
                    align="left",
                    font=("Arial", 30, "normal"))
    pen_score.penup()

    return screen, pen_score

# Function for creating cube
def create_cube():
    cube1 = Cubes()
    cube2 = Cubes()
    # Creating a list of cubes
    cubes = list()
    cubes.append(cube1)
    cubes.append(cube2)
    return cubes

# Respawn cube
def respawn_cube(x, y, cubes, pen_score, screen):
    # Checking all cubes in the list
    for cube in cubes:
        if cube.distance(x, y) < 20:
            # Increasing score
            screen.score += 1
            cube.speed(0)
            cube.setposition(random.randint(-240, 240), random.randint(250, 340))
            cube.speed(random.randint(4, 7))
            pen_score.clear()
            pen_score.goto(-250, -200)
            pen_score.write(f"Score: {screen.score}",
                            align="left",
                            font=("Arial", 30, "normal"))
            pen_score.penup()

# Movement of cubes
def move_cubes(cubes, pen_score, screen):
    try:
        while True:
            # перебор кубиков из списка
            for cube in cubes:
                cube.run(pen_score, screen)
    except:
        # try-except block used for debugging issues during game shutdown
        pass