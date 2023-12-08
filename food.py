from turtle import Turtle
import random
SCREEN_RANGE = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("crimson")
        self.speed("fastest")
        random_x = random.randint(-SCREEN_RANGE, SCREEN_RANGE)
        random_y = random.randint(-SCREEN_RANGE, SCREEN_RANGE)
        self.goto(random_x, random_y)
