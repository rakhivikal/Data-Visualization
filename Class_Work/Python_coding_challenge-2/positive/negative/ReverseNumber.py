# Program to reverse a number

# Taking input
num = int(input("Enter number: "))

# Initialize reverse
rev = 0

# Loop until number becomes 0
while num > 0:
    digit = num % 10        # get last digit
    rev = rev * 10 + digit  # build reverse
    num = num // 10         # remove last digit

# Output reversed number
print("Reverse =", rev)