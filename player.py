from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.goto(390, 0)

