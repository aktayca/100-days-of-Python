from turtle import Turtle
UP = 7.5
DOWN = -7.5
RIGHT = 7.5
LEFT = -7.5
y_list = (UP, DOWN)
x_list = (RIGHT, LEFT)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.width("20")
        self.color("white")
        self.penup()
        self.top_collision = 0
        self.paddle_collision = 0

    def move(self):
        self.x_direction = x_list[self.paddle_collision % 2]
        self.y_direction = y_list[self.top_collision % 2]
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)
