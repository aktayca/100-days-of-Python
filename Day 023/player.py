from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

PLAYER_HEIGHT_OFFSET = 10
COLLISION_X_THRESHOLD = 25
COLLISION_Y_THRESHOLD = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True

    def collision(self, car):
        player_y = self.ycor() + PLAYER_HEIGHT_OFFSET
        if ((abs(self.xcor() - car.xcor()) < COLLISION_X_THRESHOLD) and (abs(player_y - car.ycor()) < COLLISION_Y_THRESHOLD)):
            return True