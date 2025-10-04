from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


MAX_POINTS = 5

screen = Screen()
screen.bgcolor("black")

screen.setup(width=800, height=600)
side_wall = (screen.window_width()-40)/2
paddle_wall = ((screen.window_width()-135)/2)
top_wall = (screen.window_height()-40)/2

screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key= "Down", fun=r_paddle.down)
screen.onkeypress(key= "Up", fun=r_paddle.up)
screen.onkeypress(key= "s", fun=l_paddle.down)
screen.onkeypress(key= "w", fun=l_paddle.up)

#Line In The Middle
line = Turtle()
line.hideturtle()
line.pu()
line.goto(0, 300)
line.right(90)
for i in range(int(screen.window_height()/20)):
    line.color("white")
    line.pd()
    line.forward(10)
    line.pu()
    line.forward(10)

#Middle Text
middle = Turtle()
middle.color("white")
middle.hideturtle()

# Function to clear middle text after delay
def clear_middle_text():
    middle.clear()

# Function to show temporary text
def show_temporary_text(text):
    middle.write(text, None, "center", ("Courier", 24, "normal"))
    screen.ontimer(clear_middle_text, 1000)  # Clear after 1 second

game_is_on = True

while game_is_on:
    ball_speed = 0.05
    ball.home()
    round_is_on = True
    scoreboard.keep_score()
    #Game Over at MAX_POINTS
    if scoreboard.l_score == MAX_POINTS:
        middle.home()
        middle.write("Game Over. Left Wins!",None,"center",("Courier", 36, "bold"))
        round_is_on = False
        game_is_on = False
    elif scoreboard.r_score == MAX_POINTS:
        middle.home()
        middle.write("Game Over. Right Wins!",None,"center",("Courier", 36, "bold"))
        round_is_on = False
        game_is_on = False    
    while round_is_on:
        sleep(ball_speed)
        screen.update()
        ball.move()

        #Top/Bottom Wall Collission
        if ball.ycor() > (top_wall) or ball.ycor() < -top_wall:
            ball.top_collision +=1

        #Paddle Collision
        if ball.xcor() > paddle_wall and ball.distance(r_paddle)<50:
            ball.paddle_collision +=1
            if ball_speed > 0.01:
                ball_speed = ball_speed * 0.9
        elif ball.xcor() < -paddle_wall and ball.distance(l_paddle)<50:
            ball.paddle_collision +=1
            if ball_speed > 0.01:
                ball_speed = ball_speed * 0.9

        #Score Logic
        if ball.xcor() > side_wall:
            middle.pu()
            middle.goto(-150,0)
            show_temporary_text("Left Scored")
            scoreboard.l_score += 1
            ball.paddle_collision +=1
            round_is_on=False
        elif ball.xcor() < -side_wall:
            middle.pu()
            middle.goto(150,0)
            show_temporary_text("Right Scored")
            scoreboard.r_score += 1
            ball.paddle_collision +=1
            round_is_on=False

screen.exitonclick()