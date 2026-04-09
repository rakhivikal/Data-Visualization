def total_bill(items):
    return sum(items)

# Taking input from user
values = list(map(int, input("Enter values: ").split()))

print("Total Bill =", total_bill(values))