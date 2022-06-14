from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Verdana", 45, "normal"))
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Verdana", 45, "normal"))
