# Input number
num = int(input("Enter number: "))

# Check divisibility using modulus operator
if num % 3 == 0 and num % 5 == 0:
    print("Yes")   # Divisible by both
else:
    print("No")