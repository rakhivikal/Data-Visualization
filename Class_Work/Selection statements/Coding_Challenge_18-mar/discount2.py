def get_final_amount(original_amount, discount_percent):
    discount_amount = 0
    
    for i in range(int(discount_percent)):
        discount_amount += original_amount / 100
    
    final_amount = original_amount - discount_amount
    return final_amount

# Input
orig_price = float(input("Enter the original amount: "))
disc_percent = float(input("Enter discount percentage: "))

# Function call
pay_amount = get_final_amount(orig_price, disc_percent)

# Output
print("Final payable amount is:", pay_amount)