def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Function call
si = calculate_simple_interest(p, r, t)

# Output
print("Simple Interest:", si)