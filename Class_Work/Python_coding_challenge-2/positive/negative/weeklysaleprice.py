# Program to calculate total weekly sales

# Taking input (7 days sales)
sales = list(map(int, input("Enter 7 days sales: ").split()))

# Initialize total
total = 0

# Loop through sales
for s in sales:
    total += s   # add each day's sale

# Output total sales
print("Total Sales =", total)