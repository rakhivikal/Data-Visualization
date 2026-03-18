def check_eligibility(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

# Input
age = int(input("Enter age: "))

# Function call
result = check_eligibility(age)

# Output
print("Eligibility status:", result)