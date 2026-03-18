def find_total_charge(unit_input):
    rates = [(100, 5), (100, 7), (float('inf'), 10)]
    total_bill = 0
    remaining_units = unit_input

    for limit, price in rates:
        used_units = min(remaining_units, limit)
        total_bill += used_units * price
        remaining_units -= used_units
        
        if remaining_units <= 0:
            break

    return total_bill

# Input
units_entered = int(input("Enter units consumed: "))

# Function call
bill_output = find_total_charge(units_entered)

# Output
print("Total bill amount:", bill_output)