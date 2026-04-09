# Program to check whether string is palindrome

# Taking input
s = input("Enter a string: ")

# Create reverse string
rev = ""

# Loop to reverse string
for ch in s:
    rev = ch + rev

# Compare original and reversed string
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")