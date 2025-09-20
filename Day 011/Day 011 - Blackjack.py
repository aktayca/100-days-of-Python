import random
from art import logo

play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    hand_total = sum(hand)
    while hand_total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        hand_total = sum(hand)
    return hand_total


while play_game:
    print(logo)
    your_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]
    print(f"Your hand is {your_hand}, your hand total is: {calculate_score(your_hand)}.")
    print(f"Dealer's first card is {dealer_hand[0]}.")

    draw = input("Do you want to draw a card? 'Y' or 'N': ")
    while draw.upper() == "Y":
        your_hand.append(random.choice(cards))
        your_total = calculate_score(your_hand)
        print(f"Your hand is {your_hand}, your hand total is: {your_total}.")
        if your_total > 21:  # immediate bust check
            print("You bust!")
            break
        draw = input("Do you want to draw a card? 'Y' or 'N': ")

    your_total = calculate_score(your_hand)
    dealer_total = calculate_score(dealer_hand)

    if your_total <= 21:
        while dealer_total < 17:
            dealer_hand.append(random.choice(cards))
            dealer_total = calculate_score(dealer_hand)

        print(f"Dealer's hand is {dealer_hand}, dealer's total is {dealer_total}.")

        if dealer_total > 21:
            print(f"Dealer busts with {dealer_total}, you win!")
        elif your_total > dealer_total:
            print(f"Your hand is {your_total}, dealer's is {dealer_total}. You win!")
        elif your_total == dealer_total:
            print(f"Your hand is {your_total}, dealer's is {dealer_total}. It's a Draw!")
        else:
            print(f"Your hand is {your_total}, dealer's is {dealer_total}. You lose :(")

    answer = input("Play again? Type 'Y' or 'N': ").lower()
    if answer != "y":
        play_game = False
