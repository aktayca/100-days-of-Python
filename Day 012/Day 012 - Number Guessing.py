import random
from art import logo
play = "yes"
while play.lower() == "yes":
    print(logo)
    difficulty = input("What's your preferred difficulty? Easy or Hard? \n").lower()
    the_number = random.randint(1, 100)
    print("The number is between 1 and 100.")
    guess = int(input("What's your guess? \n"))
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5

    game = "yes"
    while game.lower() == "yes":
        if guess > the_number:
            print(f"Your guess is too high.")
            lives -= 1
        elif guess < the_number:
            print(f"Your guess is too low.")
            lives -= 1
        else:
            print(f"You guessed right! The number was {the_number}.")
            play = input(f"Do you want to play again? Yes or No \n").lower()
            if play == "yes":
                game = "no"
                print("\n" * 10)
                break
            else:
                play = "no"
                break

        if lives == 0:
            print(f"You are out of lives. The number was {the_number}. Game Over.")
            play = input(f"Do you want to play again? Yes or No \n")
            game = "no"
            print("\n" * 10)
            break

        print(f"You have {lives} lives left.")
        guess = int(input("What's your next guess? \n"))