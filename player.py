from turtle import Turtle


class Player(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])
        self.paddle_speed = 25

    def right_player_move_up(self):
        self.sety(self.ycor() + self.paddle_speed)

    def right_player_move_down(self):
        self.sety(self.ycor() - self.paddle_speed)

    def computer_follow_ball(self, ball):
        if ball.ycor() > self.ycor():
            self.sety(self.ycor() + 10)
        else:
            self.sety(self.ycor() - 10)

