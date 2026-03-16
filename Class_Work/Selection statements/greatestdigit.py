# Program to find the greatest digit present in a given number

# Taking input from user
num = int(input("Enter a number: "))

# Variable to store the greatest digit
greatest = 0

# Loop to check each digit
while num > 0:
    digit = num % 10      # Get the last digit
    
    if digit > greatest:  # Compare with greatest digit
        greatest = digit
    
    num = num // 10       # Remove the last digit

# Display the result
print("The greatest digit in the number is:", greatest)