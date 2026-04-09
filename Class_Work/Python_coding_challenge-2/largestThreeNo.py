# Taking three numbers as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Assume first number is largest
largest = a

# Compare with second number
if b > largest:
    largest = b

# Compare with third number
if c > largest:
    largest = c

# Display result
print("Largest =", largest)