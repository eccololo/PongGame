from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_speed = 10
        self.y_speed = 10
        self.ball_speed = 0.1

    def move(self):
        self.sety(self.ycor() + self.y_speed)
        self.setx(self.xcor() + self.x_speed)

    def get_ball_speed(self):
        return self.ball_speed

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def increase_ball_speed(self):
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()


