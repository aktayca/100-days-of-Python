#Making a list out of the "invited names" file
with open("Input/Names/invited_names.txt") as name_list: 
    names = name_list.readlines()

#Reading the template letter content and saving it to a variable.
with open("Input/Letters/starting_letter.txt", "r") as letter: 
        contents = letter.read()

for name in names:
    output_letter = contents.replace("[Name]", name.strip())
    output_folder = open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w")
    output_folder.write(output_letter)