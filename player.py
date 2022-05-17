from turtle import Turtle


class Player(Turtle):

    def __init__(self, player_pos_tuple):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.setx(10)
        self.sety(10)
        self.penup()
        self.goto(self.xcor(), self.ycor())
