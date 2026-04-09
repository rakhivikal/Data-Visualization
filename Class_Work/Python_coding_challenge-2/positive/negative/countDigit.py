# Program to count number of digits

# Taking input
num = int(input("Enter number: "))

count = 0

# Loop until number becomes 0
while num > 0:
    count += 1
    num = num // 10

# Output count
print("Number of digits =", count)