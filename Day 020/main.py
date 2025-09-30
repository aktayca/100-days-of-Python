import turtle as t
from time import sleep
import snake

ekran = t.Screen()
ekran.setup(width=600, height=600)
ekran.bgcolor("black")
ekran.title("My Snake Game")
ekran.tracer(0)
snake = snake.Snake()

ekran.listen()
ekran.onkey(key="Up", fun= snake.up)
ekran.onkey(key="Down", fun= snake.down)
ekran.onkey(key="Left", fun= snake.left)
ekran.onkey(key="Right", fun= snake.right)
# Game Loop
game_is_on = True
while game_is_on:
    ekran.update()
    sleep(0.05)  
    snake.move()
    if snake.game_over():
        snake.head.home()
        snake.head.write("Game Over!", True, align="center")
        break

ekran.exitonclick()