# Program to find the greatest number among five numbers

# Taking five numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

# Assume the first number is greatest
greatest = num1

# Compare with second number
if num2 > greatest:
    greatest = num2

# Compare with third number
if num3 > greatest:
    greatest = num3

# Compare with fourth number
if num4 > greatest:
    greatest = num4

# Compare with fifth number
if num5 > greatest:
    greatest = num5

# Display the greatest number
print("The greatest number is:", greatest)
