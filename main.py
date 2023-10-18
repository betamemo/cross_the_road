import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.addshape('images/turtle.gif')
screen.addshape('images/car.gif')
screen.bgcolor('lightyellow')
screen.tracer(0)

# init game
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# controller
screen.listen()
screen.onkeypress(fun=player.go_up, key='Up')
screen.onkeypress(fun=player.go_down, key='Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    if car_manager.is_collide(player.pos()):
        print('game over')
        scoreboard.game_over()
        game_is_on = False

    if player.is_finish():
        print('level up')
        scoreboard.level_up()

screen.exitonclick()
