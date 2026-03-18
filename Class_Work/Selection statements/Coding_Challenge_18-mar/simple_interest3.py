def interest_calc(principal_value, rate_value, time_value):
    values = [principal_value, rate_value, time_value]
    product = 1
    
    for v in values:
        product = product * v
    
    return product / 100

# Input
p_input = float(input("Enter principal amount: "))
r_input = float(input("Enter rate of interest: "))
t_input = float(input("Enter time period: "))

# Function call
si_output = interest_calc(p_input, r_input, t_input)

# Output
print("Simple Interest is:", si_output)