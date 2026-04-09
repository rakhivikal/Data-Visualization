# Program to count number of vowels in a string

# Taking input from user
text = input("Enter a string: ")

# Initialize vowel counter
count = 0

# Loop through each character
for ch in text:
    # Check if character is vowel
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1   # increase count

# Display result
print("Number of vowels =", count)