def calculate_grade(score):
    if score < 0 or score > 100:
        return 'Invalid marks'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
score = float(input("Enter the student's score: "))
grade = calculate_grade(score)
print("The student's grade is:", grade)
