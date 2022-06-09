# TODO:
#    4. Create class scoreboard and display score.
#    5. Create vertical line on a middle of the screen.
#    6. Create game end when ball move out of window.

from turtle import Screen
from player import Player
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.tracer(0)

right_player = Player((390, 0))
left_player = Player((-390, 0))
ball = Ball()

screen.listen()
screen.onkey(right_player.right_player_move_up, "Up")
screen.onkey(right_player.right_player_move_down, "Down")
screen.onkey(left_player.right_player_move_up, "w")
screen.onkey(left_player.right_player_move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(ball.get_ball_speed())
    ball.move()

    # Ball is boucing from top and bottom wall.
    if ball.ycor() >= 260 or ball.ycor() <= -260:
        ball.bounce_y()

    # Ball is bouncing from left and right paddle.
    if (ball.distance(right_player) <= 60 and ball.xcor() >= 365) or \
            (ball.distance(left_player) <= 60 and ball.xcor() <= -365):
        ball.bounce_x()
