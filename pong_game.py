# TODO:
#    1. Create class paddle or player and make it move and bounce a ball.
#    2. Create class ball and make it move and bounce from walls and players.
#    3. Create screen.
#    4. Create class scoreboard and display score.
#    5. Create vertical line on a middle of the screen.
#    6. Create game end when ball move out of window.

import turtle
from turtle import Screen

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.tracer(0)


screen.exitonclick()