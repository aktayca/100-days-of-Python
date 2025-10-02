from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-5, 280)
        self.color("white")
        
        
    def keep_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-10, 250)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))
    
    