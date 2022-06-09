from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])

