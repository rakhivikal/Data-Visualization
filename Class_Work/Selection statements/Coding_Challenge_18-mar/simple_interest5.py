def calculate_interest_value(p_amount, r_percent, t_duration):
    rate_decimal = r_percent / 100
    yearly_interest = p_amount * rate_decimal
    total_interest = yearly_interest * t_duration
    return total_interest

# Input
principal_input = float(input("Enter principal amount: "))
rate_input = float(input("Enter rate (%): "))
time_input = float(input("Enter time (years): "))

# Function call
interest_result = calculate_interest_value(principal_input, rate_input, time_input)

# Output
print("Simple Interest calculated:", interest_result)