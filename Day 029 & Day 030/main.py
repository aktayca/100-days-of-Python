from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

SAVE_PATH = "data.json"

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Lines", message="Please do not leave any fields empty.")
    else:
        confirmed = messagebox.askokcancel(title=website, message=f"E-Mail: {email}\nPassword: {password}\nDo you confirm the information?")
        if confirmed:
            try: #If Save path exists
                with open(SAVE_PATH, mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError: #If that file doesn't exist, create it
                with open(SAVE_PATH, mode="w") as data_file:
                    data = {}
                    data.update(new_data)
                    json.dump(data, data_file, indent=4)
            else: #save the updated data
                with open(SAVE_PATH, mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo(title="Saved!", message=f"Your information is saved.")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open(SAVE_PATH, mode="r") as data_file:
            content = data_file.read().strip()
            if not content:  # File is empty
                data = {}
            else:
                data_file.seek(0)
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No File", message="No passwords set yet. Please save some login credentials first.")
    else:
            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Your login credentials for {website} are:\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Sorry", message=f"We could not find any login information for {website} :(")


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
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "batuhanea@gmail.com")

pass_entry = Entry()
pass_entry.grid(column=1, row=3, sticky="ew")

#Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="ew")

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

#Column & Row Expansion

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)


window.mainloop()