import random
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        car = self.create_car()
        self.cars.append(car)
        self.counter = 0

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape('images/car.gif')
        car.goto(300, random.randint(-200, 200))
        return car

    def move(self):
        self.counter += 1
        if self.counter == 6:
            car = self.create_car()
            self.cars.append(car)
            self.counter = 0

        for c in range(len(self.cars)):
            self.cars[c].setheading(180)
            self.cars[c].forward(20)

    def is_collide(self, player_pos):
        for c in range(len(self.cars)):
            if self.cars[c].distance(player_pos) < 30:
                return True
