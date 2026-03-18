def calculate_final_price(price, discount_percent):
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount
    return final_price

# Input
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

# Function call
result = calculate_final_price(price, discount)

# Output
print("Final price after discount:", result)