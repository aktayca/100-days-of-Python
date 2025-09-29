import turtle as t

tospa = t.Turtle()
ekran = t.Screen()

def move_turtle_forwards ():
    tospa.forward(10)
def move_turtle_backwards():
    tospa.backward(10)
def turn_turtle_right():
    tospa.right(10)
def turn_turtle_left():
    tospa.left(10)
def clear_screen():
    tospa.clear()
    tospa.pu()
    tospa.home()
    tospa.pd()

ekran.listen()
ekran.onkey(key= "Up", fun= move_turtle_forwards)
ekran.onkey(key= "Down", fun= move_turtle_backwards)
ekran.onkey(key= "Right", fun= turn_turtle_right)
ekran.onkey(key= "Left", fun= turn_turtle_left)
ekran.onkey(key= "c", fun= clear_screen)









ekran.exitonclick()