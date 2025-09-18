student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades= {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 81 and student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 71 and student_scores[key] < 81:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for item in student_grades:
    print(item, ":", student_scores[item], ":", student_grades[item])
