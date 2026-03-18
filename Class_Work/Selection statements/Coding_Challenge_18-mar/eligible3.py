def eligibility_check(input_age):
    msg = ["Not Eligible", "Eligible"]
    
    if input_age >= 18:
        return msg[1]
    else:
        return msg[0]

# Input
age_val = int(input("Enter your age: "))

# Function call
output_val = eligibility_check(age_val)

# Output
print("Voting Eligibility:", output_val)