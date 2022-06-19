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

    def player_move_up(self):
        """This method moves player up"""
        self.sety(self.ycor() + self.paddle_speed)

    def player_move_down(self):
        """This method moves player down."""
        self.sety(self.ycor() - self.paddle_speed)

    def computer_follow_ball(self, ball):
        """This method assure that computer paddle will fallow ball in horizontal position."""
        if ball.ycor() > self.ycor():
            self.sety(self.ycor() + 10)
        else:
            self.sety(self.ycor() - 10)

