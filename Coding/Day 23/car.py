from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "violet", "purple", "pink", "cyan", "yellow"]
MOVE_INCREMENT = 10
START_MOVE_DISTANCE = 5


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(250, new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for each_car in self.all_cars:
            each_car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
