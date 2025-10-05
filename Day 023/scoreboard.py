from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.pu()
        self.goto(-280, 250)
    
    def keep_score(self):
        self.clear()
        self.write(f"Level: {self.level + 1}", align= "left", font=FONT)