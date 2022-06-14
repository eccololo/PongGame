from turtle import Turtle
import random


class Obstacle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=2.4, stretch_len=1)
        self.penup()
        self.x_position = random.randint(-90, 90)
        self.goto(self.x_position, -225)
