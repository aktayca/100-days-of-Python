from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.width(20)
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=0)
        self.color("white")
        self.pu()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
