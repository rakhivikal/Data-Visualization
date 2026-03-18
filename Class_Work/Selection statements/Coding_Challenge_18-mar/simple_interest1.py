def find_interest(amount, percent, duration):
    interest = amount * percent * duration
    return interest / 100

# Input
amt = float(input("Enter principal amount: "))
rate_val = float(input("Enter rate of interest: "))
time_val = float(input("Enter time period: "))

# Function call
result_interest = find_interest(amt, rate_val, time_val)

# Output
print("Calculated Simple Interest:", result_interest)