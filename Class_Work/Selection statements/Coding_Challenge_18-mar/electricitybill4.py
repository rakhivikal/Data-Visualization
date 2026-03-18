def calculate_amount(units_count):
    total_cost = 0

    for u in range(units_count):
        if u < 100:
            total_cost += 5
        elif u < 200:
            total_cost += 7
        else:
            total_cost += 10

    return total_cost

# Input
units_input_value = int(input("Enter units consumed: "))

# Function call
final_amount = calculate_amount(units_input_value)

# Output
print("Total electricity bill:", final_amount)