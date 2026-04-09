# Program to find sum of digits

# Taking input
num = int(input("Enter number: "))

# Initialize sum
total = 0

# Loop through digits
while num > 0:
    total += num % 10   # add last digit
    num = num // 10

# Output result
print("Sum of digits =", total)