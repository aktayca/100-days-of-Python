import turtle_info as ti
import turtle as t
import random

ekran = t.Screen()
ekran.bgcolor("lightgray")
ekran.setup(width= 800, height=400)
user_bet = ekran.textinput("Make Your Bet", "Who will win? ").title()
turtles = [ti.zeynep, ti.ilker, ti.batuhan, ti.melek, ti.eren, ti.cako, ti.beko]

ti.eren.teleport(-380, 150)
ti.ilker.teleport(-380, 100)
ti.zeynep.teleport(-380, 50)
ti.melek.teleport(-380, 0)
ti.batuhan.teleport(-380, -50)
ti.cako.teleport(-380, -100)
ti.beko.teleport(-380, -150)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turt in turtles:
        if turt.xcor() >= 380:
            is_race_on = False
            if user_bet == turt.name:
                print(f"You won! {turt.name} won the race!")
                break
            else:
                print(f"You lost :C {turt.name} won the race!")
                break
        turt.forward(random.randint(1,20))















ekran.exitonclick()