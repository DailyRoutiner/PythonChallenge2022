import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"]

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

passed_score = {passed_student: score for (passed_student, score) in students_score.items() if score >= 60}
print(passed_score)

# Using pandas
# Loop through a data frame
students_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"],
    "score": [50, 70, 80, 90, 30, 60]
}

student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student =="Alex":
        print( row.score)
