from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(190, 0)

