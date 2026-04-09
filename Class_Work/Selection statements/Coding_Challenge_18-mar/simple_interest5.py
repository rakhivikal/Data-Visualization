# Function to calculate Simple Interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Taking input from user
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

# Function call
result = simple_interest(p, r, t)

# Display result
print("Simple Interest is:", result)