from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.hideturtle()
        self.penup()

        
    def keep_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-130, 250)
        self.color("white")
        self.write(f"Score: {self.score}", align="right", font=("Courier", 24, "bold"))
        self.goto(-150, 220)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 24, "bold"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def get_high_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
    
    def save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))