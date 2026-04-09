# Predefined dictionary
marks = {"A": 80, "B": 95, "C": 78}

max_student = max(marks, key=marks.get)

print("Topper =", max_student)