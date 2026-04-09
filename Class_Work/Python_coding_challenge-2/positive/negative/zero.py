# Taking number input
num = int(input("Enter number: "))

# Nested if condition
if num >= 0:
    if num == 0:
        print("Zero")      # Exactly zero
    else:
        print("Positive")  # Greater than zero
else:
    print("Negative")      # Less than zero