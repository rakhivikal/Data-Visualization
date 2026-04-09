# Program to find factorial of a number

# Taking input
n = int(input("Enter number: "))

# Initialize factorial
fact = 1

# Loop from 1 to n
for i in range(1, n + 1):
    fact *= i

# Output factorial
print("Factorial =", fact)