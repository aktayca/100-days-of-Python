rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
PlayerChoice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors."))
CompChoice = random.randint(0,2)

if PlayerChoice == 0:
    print("Your Choice is: Rock")
    print(rock)
    print("-----------------------")
    if CompChoice == 0:
        print("Opponent Chose: Rock")
        print(rock)
        print("It's a Draw :/")
    elif CompChoice == 1:
        print("Opponent Chose: Paper")
        print(paper)
        print("You Lose :(")
    elif CompChoice == 2:
        print("Opponent Chose: Scissors")
        print(scissors)
        print("You Win :D")
elif PlayerChoice == 1:
    print("Your Choice is: Paper")
    print(paper)
    print("-----------------------")
    if CompChoice == 0:
        print("Opponent Chose: Rock")
        print(rock)
        print("You Win :D")
    elif CompChoice == 1:
        print("Opponent Chose: Paper")
        print(paper)
        print("It's a Draw :/")
    elif CompChoice == 2:
        print("Opponent Chose: Scissors")
        print(scissors)
        print("You Lose :(")
elif PlayerChoice == 2:
    print("Your Choice is: Scissors")
    print(scissors)
    print("-----------------------")
    if CompChoice == 0:
        print("Opponent Chose: Rock")
        print(rock)
        print("You Lose :(")
    elif CompChoice == 1:
        print("Opponent Chose: Paper")
        print(paper)
        print("You Win :D")
    elif CompChoice == 2:
        print("Opponent Chose: Scissors")
        print(scissors)
        print("It's a Draw :/")