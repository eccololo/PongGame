from turtle import Turtle
import random


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
        """This method moves the ball."""
        self.sety(self.ycor() + self.y_speed)
        self.setx(self.xcor() + self.x_speed)

    def get_ball_speed(self):
        """This method returns ball speed."""
        return self.ball_speed

    def bounce_y(self):
        """This method bounce ball in horizontal position."""
        self.y_speed *= -1

    def bounce_x(self):
        """This method bounce ball in vertical position and changes it angle slightly."""
        self.x_speed *= -1
        self.change_slightly_ball_angle()

    def increase_ball_speed(self):
        """This method changes slightly ball speed."""
        self.ball_speed *= 0.9

    def reset_ball(self):
        """This method resets ball to a starting position and speed, and adds random angle."""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
        self.change_slightly_ball_angle()

    def change_slightly_ball_angle(self):
        """This method changes slightly ball speed in random mode that ball moves in
        random angle when bounced."""
        if self.x_speed > 0 and self.y_speed > 0:
            self.x_speed = random.randint(7, 13)
            self.y_speed = random.randint(7, 13)
        elif self.x_speed < 0 and self.y_speed > 0:
            self.x_speed = random.randint(-13, -7)
            self.y_speed = random.randint(7, 13)
        elif self.x_speed > 0 and self.y_speed < 0:
            self.x_speed = random.randint(7, 13)
            self.y_speed = random.randint(-13, -7)
        else:
            self.x_speed = random.randint(-13, -7)
            self.y_speed = random.randint(-13, -7)


