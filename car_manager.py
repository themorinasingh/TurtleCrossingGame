from turtle import Turtle
import random

from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4

class CarManager:
    def __init__(self):
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        x_cor = 320
        y_cor = random.randint(-240, 240)
        car.goto(x_cor,y_cor)
        self.cars.append(car)

    def move_car(self):
        for car in self.cars :
            car.forward(self.distance)

    def speed_increase(self):
        self.distance += MOVE_INCREMENT

    def car_cleaner(self):
        for car in self.cars[:]:
            if car.xcor() < -320 :
                self.cars.remove(car)





