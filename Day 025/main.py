import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(720, 486)

turtle.shape(image)

df = pd.read_csv("50_states.csv")
states= df["state"]

text = turtle.Turtle()
text.hideturtle()
text.pu()

correct_answers = []
while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"Guess a State {len(correct_answers)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        all_states = df["state"].to_list()
        missing_states = [state for state in all_states if state not in correct_answers]
        ms = pd.DataFrame(missing_states)
        ms.to_csv("states_to_learn.csv")
        break

    if answer_state in states.values and answer_state not in correct_answers:
        matching_state = df[df["state"] == answer_state]
        answer_x = matching_state["x"].iloc[0]
        answer_y = matching_state["y"].iloc[0]
        text.goto(answer_x, answer_y)
        text.write(answer_state)
        correct_answers.append(answer_state)



turtle.mainloop()