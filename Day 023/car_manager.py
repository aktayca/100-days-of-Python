from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
GENERATION_PERCENTAGE = 20


class CarManager():
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(1, 100) <= GENERATION_PERCENTAGE:
            car = Turtle()
            car.pu()
            car.goto(random.randint(300, 315), random.randint(-240, 260))
            car.color(random.choice(COLORS))
            car.shape("square")
            car.width(5)
            car.turtlesize(stretch_wid=1, stretch_len=2, outline=None)
            self.cars.append(car)

    def move_car(self):
            for car in self.cars:
                car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor()) 
    
    def delete_car(self, removal_range):
         for car in self.cars[:]:
              if car.xcor() < -(removal_range/2):
                   self.cars.remove(car)
                   car.hideturtle()

