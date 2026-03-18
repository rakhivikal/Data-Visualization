def si_calculator(principal_amt, rate_amt, time_amt):
    total = 0
    
    for i in range(int(time_amt)):
        total += (principal_amt * rate_amt) / 100
    
    return total

# Input
p_val = float(input("Enter principal amount: "))
r_val = float(input("Enter rate of interest: "))
t_val = float(input("Enter time period: "))

# Function call
si_value = si_calculator(p_val, r_val, t_val)

# Output
print("Simple Interest:", si_value)