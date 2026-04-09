# Program to count numbers greater than 50

# Taking input
nums = list(map(int, input("Enter numbers: ").split()))

# Initialize counter
count = 0

# Loop through list
for num in nums:
    if num > 50:
        count += 1

# Output result
print("Count =", count)