def voting_status(user_age):
    status = "Not Eligible"
    if user_age >= 18:
        status = "Eligible"
    return status

# Input
age_input = int(input("Enter your age: "))

# Function call
result_status = voting_status(age_input)

# Output
print("Voting Status:", result_status)