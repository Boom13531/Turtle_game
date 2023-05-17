# Other functions
import turtle, random

# Turtle colors (randomly selected from the list)
colors = ["red", "saddle brown", "green", "dark slate blue", "purple", "White", "DarkOliveGreen", 'black']

# Spawn line of turtle
start_line = -475

# Enemy turtle class
class Enemy(turtle.Turtle):
    '''Object (enemy turtle)'''
    def __init__(self, y=0):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        turtle_color = random.choice(colors)
        colors.remove(turtle_color)
        self.color(turtle_color)
        self.penup()
        self.speed(0)
        self.goto(start_line, y)
        self.showturtle()
    def run(self):
        if self.color()[-1] != 'black':
            self.forward(random.randint(7, 21))
        # The black turtle will run faster
        else:
            self.forward(random.randint(7, 27))
# Player turtle class
class Player(Enemy):
    '''Player'''
    def __init__(self, y):
        super().__init__()
        self.color('red', 'yellow')
        self.speed(0)
        self.goto(start_line, y)

# Player object
player = Player(250)

# Enemy turtles objects
en1 = Enemy(125)
en2 = Enemy(0)
en3 = Enemy(-125)
en4 = Enemy(-250)

# Create a list for all the participants (used for iterating through them in a for loop)
participants = []
participants.extend([en1, en2, en3, en4])