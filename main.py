import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import math

#screensetup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing")

#setting up the player turtle
player = Player()

#managing cars
my_car_manager = CarManager()

#allowing the player to move up
screen.listen()
screen.onkey(key="Up",fun=player.move_forward)

#managing score
my_scoreboard = Scoreboard()

#gameplay controls
game_is_on = True
x = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()


    if x % 6 == 0:
        my_car_manager.create_car()
        #incresing amount of cars
        for i in range(0, math.floor(my_scoreboard.level/3)):
            my_car_manager.create_car()



    #moving cars
    x += 1
    my_car_manager.move_car()

    # detecting collision
    for car in my_car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
            my_scoreboard.game_over_sequence()


    #detecting player on the other side
    if player.ycor() > 280:
        player.home_state()
        my_scoreboard.message_display()
        my_car_manager.speed_increase()

    my_car_manager.car_cleaner()




screen.exitonclick()


