def bill_calculator(total_units):
    charges = 0
    i = 1
    
    while i <= total_units:
        if i <= 100:
            charges += 5
        elif i <= 200:
            charges += 7
        else:
            charges += 10
        i += 1
    
    return charges

# Input
units_value = int(input("Enter number of units: "))

# Function call
final_bill = bill_calculator(units_value)

# Output
print("Total Electricity Bill:", final_bill)