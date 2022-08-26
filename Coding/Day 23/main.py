from turtle import Screen
from player import Player
from car import Car
from scorecard import Scorecard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score = Scorecard()

screen.listen()
screen.onkey(player.move_up, "Up")
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # Detect the turtle collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            is_game_on = False

    # Detect the turtle reaches the destination without colliding
    if player.at_finish_line():
        player.go_to_start_position()
        car.level_up()
        score.increase_level()



screen.exitonclick()
