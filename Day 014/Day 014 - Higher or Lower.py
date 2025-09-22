from game_data import data
from art import logo
import random

play = "yes"
while play == "yes":
    print(logo)
    print("Welcome to the Higher or Lower game: Instagram Followers edition!")
    score = 0

    A = random.choice(data)
    B = random.choice(data)

    print("Who has the most amount of followers?")
    print(f"A - {A.get("name")}, {A.get("description")} from {A.get("country")}")
    print("OR")
    print(f"B - {B.get("name")}, {B.get("description")} from {B.get("country")}")
    guess = input("A, or B?").lower()
    if guess == "a":
        if A.get("follower_count") >= B.get("follower_count"):
            print("Your guess was correct.")
            score += 1
            print(f"{A.get("name")} has {A.get("follower_count")} thousand followers and {B.get("name")} has {B.get("follower_count")} thousand followers.")
            print(f"Your score is: {score}")
            game_loop = "yes"
        elif A.get("follower_count") < B.get("follower_count"):
            print("Your guess was wrong.")
            print(f"{B.get("name")} has {B.get("follower_count")} thousand followers and {A.get("name")} has {A.get("follower_count")} thousand followers.")
            print(f"Your score was: {score}")
            game_loop = "no"
    elif guess == "b":
        if B.get("follower_count") >= A.get("follower_count"):
            print("Your guess was correct.")
            score += 1
            print(f"{B.get("name")} has {B.get("follower_count")} thousand followers  and {A.get("name")} has {A.get("follower_count")} thousand followers.")
            print(f"Your score is: {score}")
            game_loop = "yes"
        elif B.get("follower_count") < A.get("follower_count"):
            print("Your guess was wrong.")
            print(f"{A.get("name")} has {A.get("follower_count")} thousand followers and {B.get("name")} has {B.get("follower_count")} thousand followers.")
            print(f"Your score was: {score}")
            game_loop = "no"

    while game_loop == "yes":
        A = B
        B = random.choice(data)
        print("Who has the most amount of followers?")
        print(f"A - {A.get("name")}, {A.get("description")} from {A.get("country")}")
        print("OR")
        print(f"B - {B.get("name")}, {B.get("description")} from {B.get("country")}")
        guess = input("A, or B?").lower()
        if guess == "a":
            if A.get("follower_count") >= B.get("follower_count"):
                print("Your guess was correct.")
                score += 1
                print(f"{A.get("name")} has {A.get("follower_count")} and {B.get("name")} has {B.get("follower_count")}.")
                print(f"Your score is: {score}")
            elif A.get("follower_count") < B.get("follower_count"):
                print("Your guess was wrong.")
                print(f"{B.get("name")} has {B.get("follower_count")} thousand followers and {A.get("name")} has {A.get("follower_count")} thousand followers.")
                print(f"Your score was: {score}")
                game_loop = "no"
        elif guess == "b":
            if B.get("follower_count") >= A.get("follower_count"):
                print("Your guess was correct.")
                score += 1
                print(f"{B.get("name")} has {B.get("follower_count")} thousand followers  and {A.get("name")} has {A.get("follower_count")} thousand followers.")
                print(f"Your score is: {score}")
            elif B.get("follower_count") < A.get("follower_count"):
                print("Your guess was wrong.")
                print(f"{A.get("name")} has {A.get("follower_count")} thousand followers  and {B.get("name")} has {B.get("follower_count")} thousand followers.")
                print(f"Your score was: {score}")
                game_loop = "no"
    play = input("Do you want to play again? Type 'Yes' or 'No'").lower()