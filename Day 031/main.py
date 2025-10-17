from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
STARTING_LANGUAGE_FONT = ("Arial", 35, "bold")
STARTING_WORD_FONT = ("Arial", 25, "italic")

#---------WINDOW-----------

window = Tk()
window.title("Yoonki")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#---------DATA-----------

df = pd.read_csv("data/french_words.csv")
dictionary = df.to_dict(orient="records")
session_words = dictionary[:]

current_index = 0
word_pair = session_words[current_index]
l1_name = df.columns.values.tolist()[0] #Gets the index 0 from the column name list
l2_name = df.columns.values.tolist()[1]
l1_word = word_pair[l1_name]
l2_word = word_pair[l2_name]

#---------IMAGES-----------

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

#---------FUNCTIONS-----------

flip_timer = None
def new_word(): #Will take this word out of the list for the session if you memorized it
    global word_pair, current_index, flip_timer

    if len(session_words)>0:
        current_index = rd.randrange(len(session_words))
        word_pair = session_words[current_index]

        l1_word = word_pair[l1_name]
        l2_word = word_pair[l2_name]

        canvas.itemconfig(card, image= card_front_img)
        canvas.itemconfig(lang_label, text = l1_name, fill="black")
        canvas.itemconfig(word_label, text = l1_word, fill="black")
        canvas.itemconfig(info_label, fill="black")

        def flip_card(): #After 3 seconds, change the card colour and show the translations
            global word_pair

            canvas.itemconfig(card, image= card_back_img)
            canvas.itemconfig(lang_label, text = l2_name, fill="white")
            canvas.itemconfig(word_label, text = l2_word, fill="white")
            canvas.itemconfig(info_label, fill="white")

        if flip_timer:
            window.after_cancel(flip_timer)
        flip_timer = window.after(3000, flip_card)

    else:
        canvas.itemconfig(card, image= card_back_img)
        canvas.itemconfig(lang_label, text = "Congratulations!", fill="white",font=("Arial", 35, "bold"))
        canvas.itemconfig(word_label, text = "You made it to the end of the list!\nDo you want to restart?", fill="white",font=("Arial", 25, "italic"))


        right_button.grid_remove()
        wrong_button.grid_remove()
        start_button.config(text="Restart")
        start_button.grid(column=0, row=1, columnspan=2, sticky="ew")

def pop_word():
    global word_pair
    session_words[current_index], session_words[-1] = session_words[-1], session_words[current_index]
    session_words.pop()

def b_right():
    pop_word()
    new_word()

def b_wrong():
    new_word()

def b_start():
    canvas.itemconfig(lang_label, font=LANGUAGE_FONT)
    canvas.itemconfig(word_label, font=WORD_FONT)
    global session_words
    
    start_button.grid_remove()
    right_button.grid(column=1, row=1)
    wrong_button.grid(column=0, row=1)
    
    if len(session_words) == 0: #Only make a shallow copy if the word list is empty
        session_words = dictionary[:]
    new_word()

#---------UI SETUP-----------

canvas = Canvas(width=800, height=526, highlightthickness=0, background= BACKGROUND_COLOR ,highlightbackground=BACKGROUND_COLOR)

card = canvas.create_image(400, 263, image= card_front_img)

canvas.grid(column=0, row=0, columnspan=2)

#Buttons

start_button =Button(text= "START", highlightthickness=0, background=BACKGROUND_COLOR,fg= "black", font=("Arial", 24, "bold"), command= b_start)
start_button.grid(column=0, row=1, columnspan=2, sticky="ew")

right_button = Button(image=right_img, highlightthickness=0, background=BACKGROUND_COLOR, command=b_right)
wrong_button = Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, command=b_wrong)

#Starting Text
lang_label = canvas.create_text(400, 150, text="Welcome to Yoonki", font=STARTING_LANGUAGE_FONT, fill="black")
word_label = canvas.create_text(400, 263, text="Press Any Button to Start", font=STARTING_WORD_FONT)
##Instructions
info_label = canvas.create_text(400, 400, text="After the card flips,\nPress Tick(✓) if you got it right.\nPress Cross(✗) if you couldn't get it right.\n" \
"Words you got right will be removed from the session.", font=("Arial", 14, "normal"), fill="black", anchor="center", justify="center")

#Mainloop
window.mainloop()