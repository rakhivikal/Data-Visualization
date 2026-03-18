def payable_value(total_price, discount_percent):
    discount_fraction = float(discount_percent) / 100
    saved_amount = sum([total_price * discount_fraction])
    final_pay = total_price - saved_amount
    return final_pay

# Input
price_val = float(input("Enter total price: "))
disc_val = float(input("Enter discount percentage: "))

# Function call
result_amount = payable_value(price_val, disc_val)

# Output
print("Final payable price:", result_amount)