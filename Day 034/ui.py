from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.wn = Tk()
        self.wn.title("Quizzly Bear")
        self.wn.minsize(width=350, height=500)
        self.wn.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="ew", pady= 40, padx=20)

        def button_func(answer):
            is_correct = quiz_brain.check_answer(answer)
            if is_correct:
                self.canvas.config(background="green")
            else:
                self.canvas.config(background="red")
            if quiz_brain.still_has_questions():
                self.canvas.after(1000, lambda: self.canvas.config(background="white"))
                self.get_next_question()
            else:
                self.canvas.after(1000, lambda: self.canvas.config(background="white"))
                true_button.config(state="disabled")
                false_button.config(state="disabled")
                self.canvas.itemconfig(self.question_text, text= f"Congratulations! Your Final score was {quiz_brain.score}/10")
            score_label.config(text=f"Score: {quiz_brain.score}")

        #Photo Creation
        false_img = PhotoImage(file="images/false.png")
        true_img =  PhotoImage(file="images/true.png")

        #Button Creation
        false_button = Button(image=false_img, command= lambda: button_func("false"))
        true_button = Button(image=true_img, command= lambda: button_func("true"))
        
        #Button Grids
        false_button.grid(column=1, row=2)
        true_button.grid(column=0, row= 2)

        self.question_text = self.canvas.create_text((150, 125), text="Hello", font=("Arial", 20, "italic"), width= 200)
        score_label = Label(self.wn, text=f"Score: {quiz_brain.score}", font=("Arial", 14, "bold"), background=THEME_COLOR, foreground="white",)
        score_label.grid(column=1, row=0)

        self.get_next_question()

        self.wn.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)