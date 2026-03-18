def compute_bill(unit_used):
    total = 0
    
    if unit_used > 200:
        total = (100 * 5) + (100 * 7) + ((unit_used - 200) * 10)
    elif unit_used > 100:
        total = (100 * 5) + ((unit_used - 100) * 7)
    else:
        total = unit_used * 5
    
    return total

# Input
units_input = int(input("Enter total units consumed: "))

# Function call
bill_amount = compute_bill(units_input)

# Output
print("Electricity Bill:", bill_amount)