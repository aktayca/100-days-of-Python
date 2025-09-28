import turtle
import random

tospa = turtle.Turtle()
ekran = turtle.Screen()

tospa.shape("turtle")
ekran.colormode(255)
tospa.pensize(1)
tospa.speed("fastest")

## DASHED LINES
# def dashed_line(length):
#     for i in range(int(length/20)):
#         tospa.pd()
#         tospa.fd(10)
#         tospa.pu()
#         tospa.fd(10)

# dashed_line(200)
# tospa.backward(200)

# # MANYGONS
# tospa.pu()
# tospa.goto(-50, (307.77/2))
# tospa.pd()
# def manygons(sides):
#     for i in range(sides):
#         tospa.fd(100)
#         tospa.right(360/sides)
#         print(tospa.pos())

# for i in range(3, 11):
#     tospa.color((random.randint(1, 255)), (random.randint(1, 255)), (random.randint(1, 255)))
#     manygons(i)

#RANDOM WALK

# def random_walk():
#     tospa.shape("arrow")
#     tospa.speed("fastest")
#     tospa.pensize(15)

#     while True:
#         directions = random.choice([0, 90, 180, 270])
#         tospa.color((random.randint(1, 255)), (random.randint(1, 255)), (random.randint(1, 255)))
#         tospa.setheading(directions)
#         tospa.fd(35)

# random_walk()

while True:
    tospa.color((random.randint(1, 255)), (random.randint(1, 255)), (random.randint(1, 255)))
    tospa.right(5)
    tospa.circle(100)

ekran.exitonclick()

