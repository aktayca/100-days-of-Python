import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

again = True

while again:
        word = input("\nWhat do you want to spell in NATO alphabet? ")
        word_upper = word.upper()
        letter_list = [letter for letter in word_upper]
        try:
            result = [nato_dict[letter] for letter in letter_list]
        except KeyError:
            print("Only letters in the alphabet please!")
        else:
            print(f"You can spell {word} as {result} in the NATO Phonetic Alphabet.")
        finally:
            i = input(f"\nDo you want to convert another word? Y/N  ").upper()
            if i == "Y":
                continue
            else:
                    again = False