# TODO:
#    1. Make game end.

from turtle import Screen
from player import Player
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from obstacle import Obstacle

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.tracer(0)

right_player = Player((390, 0), "blue")
computer = Player((-390, 0), "green")
ball = Ball()
scoreboard = Scoreboard()
obstacle = Obstacle()

screen.listen()
screen.onkey(right_player.player_move_up, "Up")
screen.onkey(right_player.player_move_down, "Down")
screen.onkey(computer.player_move_up, "w")
screen.onkey(computer.player_move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(ball.get_ball_speed())
    ball.move()
    obstacle.move()
    computer.computer_follow_ball(ball)

    if scoreboard.r_score >= 5 or scoreboard.l_score >= 5:
        scoreboard.end_game()
        sleep(5)
        game_is_on = False

    # Ball is boucing from top and bottom wall.
    if ball.ycor() >= 260 or ball.ycor() <= -260:
        ball.bounce_y()

    # Ball is bouncing from left and right paddle.
    if (ball.distance(right_player) <= 60 and ball.xcor() >= 365) or \
            (ball.distance(computer) <= 60 and ball.xcor() <= -365):
        ball.bounce_x()
        ball.increase_ball_speed()

    # Ball is bouncing from obstacle when two collide
    if (ball.distance(obstacle) <= 40 and ball.xcor() <= (obstacle.xcor() - 10)) \
            or (ball.distance(obstacle) <= 40 and ball.xcor() >= (obstacle.xcor() + 10)):
        ball.bounce_x()

    # When ball is passing right or left wall its starts over again from middle of the screen and
    # with opposite direction.
    if ball.xcor() <= -450:
        ball.reset_ball()
        scoreboard.r_score_point()
    elif ball.xcor() >= 450:
        ball.reset_ball()
        scoreboard.l_score_point()
