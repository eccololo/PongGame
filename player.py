from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])
        self.paddle_speed = 25

    def right_player_move_up(self):
        self.sety(self.ycor() + self.paddle_speed)

    def right_player_move_down(self):
        self.sety(self.ycor() - self.paddle_speed)

