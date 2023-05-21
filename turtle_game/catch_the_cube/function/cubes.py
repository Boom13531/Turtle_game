# Other functions
import turtle
import random


class Cubes(turtle.Turtle):
    '''Class for game cubes'''

    def __init__(self):
        super().__init__(shape='square')
        self.color('red', 'yellow')
        self.penup()
        # Random speed (from 4 to 7)
        self.speed(random.randint(4, 7))
        # Random goto (x coordinate from -240 to 240, y coordinate = 300)
        self.goto(random.randint(-240, 240), 300)

    # Game function
    def run(self, pen_score, screen):
        self.goto(self.xcor(), self.ycor() - self.speed())
        # Check if cube has touched the boundary
        if self.ycor() <= -140:
            pen_score.clear()
            pen_score.goto(-250, -200)
            pen_score.write(f"Ира окончена счёт: {screen.score}", align="left", font=("Arial", 30, "normal"))
            pen_score.penup()
            turtle.exitonclick()


# Function for creating a cube
def create_cube():
    cube1 = Cubes()
    cube2 = Cubes()
    # Create a list of cubes
    cubes = list()
    cubes.append(cube1)
    cubes.append(cube2)
    return cubes