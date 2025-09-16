import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
while not game_over:
    print(f"{lives} Lives Left")
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if "_" not in display:
        game_over = True
        print("Congratulations! You Win!")

    print(stages[lives])
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(stages[0])
            print(f"You are out of lives. The word you were trying to guess was {chosen_word}.")

    if guess in guessed_letters:
        print("You have already guessed this letter.")
    guessed_letters.append(guess)