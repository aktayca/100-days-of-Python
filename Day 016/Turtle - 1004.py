import turtle

screen = turtle.Screen()
screen.bgcolor("#400026")
screen.title("MELEK in Turtle Graphics")

pen = turtle.Turtle()
pen.speed(4)
pen.color("pink")
pen.shape("turtle")
pen.pensize(15)

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


pen.penup()
pen.speed(10)
pen.goto(-600, 0)
pen.speed(1)
pen.forward(200)
pen.goto(-200, 0)
pen.speed(4)
pen.pendown()

# M
pen.left(90)
pen.forward(100)
pen.right(135)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.right(135)
pen.forward(100)

# Move to E1
pen.penup()
pen.left(90)
pen.forward(30)
pen.pendown()

# E1
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(40)
pen.backward(40)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(30)
pen.backward(30)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(40)

# Move to position for L
pen.penup()
pen.forward(30)
pen.pendown()

# Draw the letter L
pen.left(90)
pen.forward(100)
pen.backward(100)
pen.right(90)
pen.forward(40)

# Move to E2
pen.penup()
pen.forward(30)
pen.pendown()

# E2
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(40)
pen.backward(40)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(30)
pen.backward(30)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(40)

# Move to K
pen.penup()
pen.forward(30)
pen.pendown()

# K

pen.left(90)
pen.forward(100)
pen.backward(60)
pen.right(45)
pen.forward(84.85)
pen.backward(65)
pen.right(95)
pen.forward(72)
pen.penup()
pen.left(50)
pen.speed(10)
pen.goto(0, -215)

# Heart
heart()
pen.color("pink")
pen.right(130)
pen.speed(1)
pen.forward(90)

screen.exitonclick()