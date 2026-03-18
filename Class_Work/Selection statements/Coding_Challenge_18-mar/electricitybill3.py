def electricity_amount(u_value):
    charges_list = [5, 7, 10]
    
    if u_value <= 100:
        index = 0
    elif u_value <= 200:
        index = 1
    else:
        index = 2
    
    total_amount = u_value * charges_list[index]
    return total_amount

# Input
units_data = int(input("Enter consumed units: "))

# Function call
bill_result = electricity_amount(units_data)

# Output
print("Amount to be paid:", bill_result)