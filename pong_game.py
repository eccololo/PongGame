# TODO:
#    1. Create class paddle or player and make it move and bounce a ball.
#    2. Create class ball and make it move and bounce from walls and players.
#    4. Create class scoreboard and display score.
#    5. Create vertical line on a middle of the screen.
#    6. Create game end when ball move out of window.

import turtle
from turtle import Screen
from player import Player

PLAYER_1_START_POSITION = (300, 0)
PLAYER_2_START_POSITION = (-300, 0)

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.tracer(0)

player1 = Player(PLAYER_1_START_POSITION)
player2 = Player(PLAYER_2_START_POSITION)

game_is_on = True

while game_is_on:
    pass


screen.exitonclick()