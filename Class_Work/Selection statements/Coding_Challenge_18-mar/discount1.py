def find_payable_amount(cost, discount_rate):
    discount_value = discount_rate / 100
    payable = cost * (1 - discount_value)
    return payable

# Input
cost = float(input("Enter original price: "))
disc = float(input("Enter discount rate (%): "))

# Function call
final_amount = find_payable_amount(cost, disc)

# Output
print("Amount to be paid after discount:", final_amount)