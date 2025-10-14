from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

SAVE_PATH = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    pass_letters = [choice(letters) for _ in range(nr_letters)]
    pass_symbols = [choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_numbers + pass_letters + pass_symbols

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    pass_entry.delete(0,END)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Lines", message="Please do not leave any fields empty.")
    else:
        confirmed = messagebox.askokcancel(title=website, message=f"E-Mail: {email}\nPassword: {password}\nDo you confirm the information?")
        if confirmed:
            with open(SAVE_PATH, mode="a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo(title="Saved!", message=f"Your information was saved to the {SAVE_PATH}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=20, pady=20,)


logo = PhotoImage(file="images/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image= logo)
canvas.grid(column=1, row= 0)

#Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row= 1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row= 2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row= 3)

#Entries

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "batuhanea@gmail.com")

pass_entry = Entry()
pass_entry.grid(column=1, row=3, sticky="ew")

#Buttons

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

#Column & Row Expansion

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)


window.mainloop()