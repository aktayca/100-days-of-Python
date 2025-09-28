import turtle as t
import random
# import colorgram


# colors = colorgram.extract('images/hirstPaintingOG.png', 50)
tospa = t.Turtle()
ekran = t.Screen()
ekran.colormode(255)

# rgb_colors = []
# old = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     old.append(new_color)

# print(old)

# Hirst's Spot Painting
ekran.bgcolor((245, 241, 233))
rgb_colors = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (25, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 183), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 100), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59), (172, 204, 182), (108, 46, 38), (159, 204, 215), (76, 69, 37), (9, 87, 109)]
tospa.pu()
tospa.hideturtle()
tospa.speed("fastest")
for i in range(10):
    tospa.teleport(-250, i * 50 - 200)
    for i in range(10):
        tospa.color(random.choice(rgb_colors))
        tospa.dot(20)
        tospa.fd(50)

ekran.exitonclick()