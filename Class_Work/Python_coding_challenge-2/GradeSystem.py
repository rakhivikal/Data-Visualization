# Taking marks input
marks = int(input("Enter marks: "))

# Checking grade using ranges
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")