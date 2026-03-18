def compute_payable_amount(amount_value, discount_value):
    discount_amount = 0
    step = amount_value / 100
    
    count = 0
    while count < discount_value:
        discount_amount += step
        count += 1
    
    final_result = amount_value - discount_amount
    return final_result

# Input
amount_input = float(input("Enter total price: "))
disc_input = int(input("Enter discount percentage: "))

# Function call
output_amount = compute_payable_amount(amount_input, disc_input)

# Output
print("Final amount to pay:", output_amount)