# Program to check whether a number is divisible by 100 or not

# take input from user
num = int(input("Enter a number: "))

# check condition
if num % 100 == 0:
    # if remainder is 0
    print("Number is divisible by 100")
else:
    # if remainder is not 0
    print("Number is not divisible by 100")