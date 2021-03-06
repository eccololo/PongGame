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
        self.y_speed = 10

    def move(self):
        """This method moves obstacle from bottom to top of the window."""
        self.sety(self.ycor() + self.y_speed)

        if self.ycor() > 300:
            self.set_proper_position()

    def set_proper_position(self):
        """This method randomise x starting position of an obstacle."""
        self.goto(random.randint(-90, 90), -300)
