from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer

    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="POMODORO", font=(FONT_NAME, 30, "bold"), fg= DARK_GREEN, bg= YELLOW)
    timer = 0

    focus1_label.config(text="□", fg=RED)
    focus2_label.config(text="□", fg=RED)
    focus3_label.config(text="□", fg=RED)
    focus4_label.config(text="□", fg=RED)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global timer
    global reps
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    timer = 1

    reps += 1

    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    work_secs = WORK_MIN * 60

    if reps > 8:
        reset_timer()
        return
    elif reps % 8 == 0:
        secs = long_break_secs
        title.config(text="YOU EARNED IT. TAKE A LONG BREAK!", font=(FONT_NAME, 30, "bold"), fg= RED, bg= YELLOW)
    elif reps % 2 == 0:
        secs = short_break_secs
        title.config(text="BREAK TIME", font=(FONT_NAME, 30, "bold"), fg= PINK, bg= YELLOW)
    else:
        secs = work_secs
        title.config(text="WORK TIME!", font=(FONT_NAME, 30, "bold"), fg= DARK_GREEN, bg= YELLOW)

    if reps == 2:  # After first work
        focus1_label.config(text="✓", fg=DARK_GREEN)
    elif reps == 4:  # After second work
        focus2_label.config(text="✓", fg=DARK_GREEN)
    elif reps == 6:  # After third work
        focus3_label.config(text="✓", fg=DARK_GREEN)
    elif reps == 8:  # After fourth work
        focus4_label.config(text="✓", fg=DARK_GREEN)

    count_down(secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    if timer == 0:
        return

    count_min = count//60
    count_secs = count%60

    if count_secs == 0:
        count_secs = "00"

    if int(count_secs) <10 and count_secs != "00":
        count_secs = f"0{count_secs}"

    if int(count_min) <10:
        count_min = f"0{count_min}"
        
    if count > 0:
        window.after(10, count_down, count-1)
    else:
        start_timer()

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

tomato = PhotoImage(file="images/tomato.png")

title = Label(text="POMODORO", font=(FONT_NAME, 30, "bold"), fg= DARK_GREEN, bg= YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image= tomato)
timer_text = canvas.create_text(102,130, text="00:00",fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

#Buttons

start_button = Button(text="Start", font=("Calibri", 14, "bold"), fg= RED, bg=GREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Calibri", 14, "bold"), fg= RED, bg=GREEN, command=reset_timer)
reset_button.grid(column=5, row=2)

#Checkboxes

tick_frame = Frame()
tick_frame.grid(column=1, row=4)

focus1_label = Label(tick_frame, text="□", font=(FONT_NAME, 20), fg=RED, bg=YELLOW)
focus1_label.grid(column=1, row=4)

focus2_label = Label(tick_frame, text="□", font=(FONT_NAME, 20), fg=RED, bg=YELLOW)  
focus2_label.grid(column=2, row=4)

focus3_label = Label(tick_frame, text="□", font=(FONT_NAME, 20), fg=RED, bg=YELLOW)
focus3_label.grid(column=3, row=4)

focus4_label = Label(tick_frame, text="□", font=(FONT_NAME, 20), fg=RED, bg=YELLOW)
focus4_label.grid(column=4, row=4)

# Instructions
instructions = Label(text="Click 'Start Pomodoro' to begin!\n\nDon't minimize(The _ button),\nJust click to the background.", 
                    font=(FONT_NAME, 10), fg=RED, bg=YELLOW, justify=CENTER)
instructions.grid(column=1, row=5, pady=10)

window.mainloop()