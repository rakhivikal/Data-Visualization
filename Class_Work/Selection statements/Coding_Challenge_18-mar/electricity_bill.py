def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10
    return bill

# Input
units = int(input("Enter units consumed: "))

# Function call
total_bill = calculate_electricity_bill(units)

# Output
print("Total bill amount:", total_bill)