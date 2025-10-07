import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen_width = 600
screen_buffer = 100
screen_height = 600
screen = Screen()
screen.setup(width=600, height=600)
screen.screensize(500, 500)
screen.tracer(0)
score = Scoreboard()
player = Player()
cars = CarManager()
screen.bgcolor("lightgray")
screen.listen()
screen.onkey(fun=player.move, key= "Up")

min_sleep_time = 0.003
sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    score.keep_score() #Score
    cars.create_car() #Car Creation
    cars.move_car() #Car Movement
    cars.delete_car(screen_width + screen_buffer)
    if player.finish(): #Level Up
        score.level += 1
        if sleep_time >= min_sleep_time:
            sleep_time = sleep_time*0.7
    for car in cars.cars:
        if player.collision(car):
            game_is_on = False

    screen.update()


screen.exitonclick()