""" 5. Find the grade of a student based on five different subjects and the gradation table is given below:
Average Mark     Grade
91-100             O
81-90              A+
71-80              A
61-70              B
51-60              C
41-50              D
33-40              E
Less than 33       F
"""

sum_marks = 0
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    sum_marks += m
avg = sum_marks / 5
if avg<0 or avg>100:
    grade = "INVALID!"
elif avg >= 91:
    grade = "O"
elif avg >= 81:
    grade = "A+"
elif avg >= 71:
    grade = "A"
elif avg >= 61:
    grade = "B"
elif avg >= 51:
    grade = "C"
elif avg >= 41:
    grade = "D"
elif avg >= 33:
    grade = "E"
else:
    grade = "F"
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")