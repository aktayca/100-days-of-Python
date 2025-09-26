from question_model import Question
from data import question_data
import quiz_brain 


question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()