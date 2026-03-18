def compute_si(p_amt, r_rate, t_time):
    temp = p_amt * t_time
    interest_value = (temp * r_rate) / 100
    return interest_value

# Input
principal_val = float(input("Enter principal: "))
rate_val = float(input("Enter rate: "))
time_val = float(input("Enter time: "))

# Function call
si_result = compute_si(principal_val, rate_val, time_val)

# Output
print("Simple Interest is:", si_result)