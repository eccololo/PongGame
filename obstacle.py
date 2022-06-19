from turtle import Turtle
import random


class Obstacle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=2.4, stretch_len=1)
        self.penup()
        self.set_proper_position()
        # self.x_position = random.randint(-90, 90)
        # self.goto(self.x_position, -300)
        self.y_speed = 10

    def move(self):
        self.sety(self.ycor() + self.y_speed)

        if self.ycor() > 300:
            self.set_proper_position()

    def set_proper_position(self):
        self.goto(random.randint(-90, 90), -300)
