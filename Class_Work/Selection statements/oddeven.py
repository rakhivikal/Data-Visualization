# Function to check odd or even
def check_even_odd(num):
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

# Taking input from user
number = int(input("Enter a number: "))

# Calling the function
check_even_odd(number)
