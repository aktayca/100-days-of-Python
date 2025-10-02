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
snake = snake.Snake()
food = Food()
score = Scoreboard()

ekran.listen()
ekran.onkey(key="Up", fun= snake.up)
ekran.onkey(key="Down", fun= snake.down)
ekran.onkey(key="Left", fun= snake.left)
ekran.onkey(key="Right", fun= snake.right)
# Game Loop
game_is_on = True
sleep_time = 0.05
while game_is_on:
    ekran.update()
    sleep(sleep_time)  
    snake.move()
    score.keep_score()
    if snake.collision():
        snake.head.home()
        snake.head.write("Game Over!", True, align="center")
        break

    #Food Acquired
    if snake.head.distance(food) < 17: 
        food.refresh()
        score.score += 1
        snake.extend()
        sleep_time -= 0.0005
    
    
ekran.exitonclick()