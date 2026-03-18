def amount_after_cut(base_price, cut_percent):
    remaining_percent = 100 - cut_percent
    final_value = (base_price * remaining_percent) / 100
    return final_value

# Input
price_input = float(input("Enter price value: "))
discount_input = float(input("Enter discount %: "))

# Function call
ans1 = amount_after_cut(price_input, discount_input)

# Output
print("Payable amount:", ans1)