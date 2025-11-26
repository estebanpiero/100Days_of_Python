student_grades = {}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        grade = 'Outstanding'
    elif score >= 81:
        grade = 'Exceeds Expectations'
    elif score >= 71:
        grade = 'Acceptable'
    else:
        grade = 'Fail'
#    print(f"{student}: {grade}")
    student_grades[student] = grade

print(student_grades)
