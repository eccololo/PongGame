from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(100, 100)
        self.write("Hello World", align="center", font=("Verdana", 15, "normal"))
