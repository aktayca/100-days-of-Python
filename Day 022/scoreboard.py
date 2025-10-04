from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-100, 180)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "bold"))

    def keep_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "bold"))
        
