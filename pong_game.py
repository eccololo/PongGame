# TODO:
#    1. Create class paddle or player and make it move and bounce a ball.
#    2. Create class ball and make it move and bounce from walls and players.
#    4. Create class scoreboard and display score.
#    5. Create vertical line on a middle of the screen.
#    6. Create game end when ball move out of window.

from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=900, height=550)
screen.bgcolor("black")
screen.tracer(0)

right_player = Player((390, 0))
left_player = Player((-390, 0))

screen.listen()
screen.onkey(right_player.right_player_move_up, "up")
screen.onkey(right_player.right_player_move_down, "down")

game_is_on = True

while game_is_on:
    screen.update()
