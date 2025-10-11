from tkinter import *

window = Tk()
window.title("Temperature Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)


conversion_direction = "c_to_f"

# Labels
celc_label = Label(text="Celcius", font=("Calibri", 12, "bold"))
celc_label.grid(column=2, row=0, sticky="w")
celc_label.config(padx=10, pady=10)

fahr_label = Label(text="Fahrenheit", font=("Calibri", 12, "bold"))
fahr_label.grid(column=2, row=1, sticky="w")
fahr_label.config(padx=10, pady=10)

result_label = Label(text="is equal to", font=("Calibri", 12))
result_label.grid(column=0, row=1)

output_value = Label(text=" ", font=("Calibri", 12, "bold"))
output_value.grid(column=1, row=1)

# Entry
input_entry = Entry()
input_entry.config(width=10, justify="center")
input_entry.grid(column=1, row=0)

# Swap func
def swap_conversion():
    global conversion_direction
    if conversion_direction == "c_to_f":
        conversion_direction = "f_to_c"
        celc_label.config(text="Fahrenheit")
        fahr_label.config(text="Celcius")
        result_label.config(text="is equal to")
    else:
        conversion_direction = "c_to_f"
        celc_label.config(text="Celcius") 
        fahr_label.config(text="Fahrenheit")
        result_label.config(text="is equal to")

    input_entry.delete(0, END)
    output_value.config(text=" ")

# Calculation func
def button_clicked():
    try:
        if input_entry.get() == "":
            output_value["text"] = "Where's the value to convert you donut?"
        else:
            temp_value = float(input_entry.get())
            if conversion_direction == "c_to_f":
                result = (temp_value * 9/5) + 32
            else:
                result = (temp_value - 32) * 5/9
            output_value["text"] = round(result, 2)
    except ValueError:
        output_value["text"] = "I'm afraid I only speak in digits :("

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(width=9)

# Swap
swap_button = Button(text="↕ Swap", command=swap_conversion)
swap_button.grid(column=2, row=2)
swap_button.config(width=6)

window.mainloop() 