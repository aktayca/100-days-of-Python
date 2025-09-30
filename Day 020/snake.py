from turtle import Screen, Turtle

STARTING_POSITIONS = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(pos)
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range((len(self.segments) -1) ,0,-1):
            new_pos = self.segments[seg_num -1].pos()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def game_over(self):
        if self.head.xcor() >= 300:
            return True
        elif self.head.ycor() >= 300:
            return True
    