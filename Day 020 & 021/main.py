from turtle import Screen
from time import sleep
import snake
from food import Food
from scoreboard import Scoreboard

ekran = Screen()
ekran.setup(width=600, height=600)
ekran.bgcolor("black")
ekran.title("My Snake Game")
ekran.tracer(0)
snakey = snake.Snake()
food = Food()
score = Scoreboard()

ekran.listen()
ekran.onkey(key="Up", fun= snakey.up)
ekran.onkey(key="Down", fun= snakey.down)
ekran.onkey(key="Left", fun= snakey.left)
ekran.onkey(key="Right", fun= snakey.right)
# Game Loop
game_is_on = True
sleep_time = 0.05
while game_is_on:
    ekran.update()
    sleep(sleep_time) 
    snakey.move()
    score.keep_score()
    if snakey.collision():
        score.save_high_score()
        score.reset()
        snakey.reset()
        sleep_time = 0.05
    #Food Acquired
    if snakey.head.distance(food) < 17: 
        food.refresh()
        score.score += 1
        snakey.extend()
        sleep_time -= 0.0005
    
ekran.exitonclick()