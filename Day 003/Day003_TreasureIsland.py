print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You came across a fork. Do you go left or right?: ")
Fork = input("Type \"left\" to go left. Type \"right\" to go right.\n")
if Fork.lower() != "left":
    print("You fell into a hole. Game Over")
    exit()

print("You've come to a lake. There is an island in the middle of the lake.")
Lake = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
if Lake.lower() != "wait":
    print("You were attacked by a shark. Game Over.")
    exit()

print("You came across three doors. Their colours are red, blue and yellow.")
Door = input("Type the colour of the door you want to go in.\n")
if Door.lower() == "red":
    print("You were killed by fire.")
    print("Game Over")
    exit()
elif Door.lower() == "blue":
    print("You died due to extreme cold.")
    print("Game Over")
    exit()
elif Door.lower() == "yellow":
    print("The bright yellow of the gold welcomes you.")
    print("You Won!")
    exit()
else:
    print("Medical teams rescue you out because you had a concussion and chose a door that does not exist.")
    print("Game Over")
    exit()