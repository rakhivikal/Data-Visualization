# Program to check palindrome number

# Taking input
num = int(input("Enter number: "))

temp = num   # store original number
rev = 0

# Reverse number
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

# Compare original and reverse
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")