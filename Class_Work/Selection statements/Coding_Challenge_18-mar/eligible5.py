def get_voting_result(age_input_value):
    eligibility_map = {True: "Eligible", False: "Not Eligible"}
    condition = age_input_value >= 18
    return eligibility_map[condition]

# Input
user_age_input = int(input("Enter your age: "))

# Function call
final_output = get_voting_result(user_age_input)

# Output
print("Voting Result:", final_output)