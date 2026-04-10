# Program to find maximum number in list

# Taking input
nums = list(map(int, input("Enter numbers: ").split()))

# Assume first element is maximum
max_val = nums[0]

# Loop through list
for num in nums:
    if num > max_val:
        max_val = num

# Output result
print("Maximum =", max_val)