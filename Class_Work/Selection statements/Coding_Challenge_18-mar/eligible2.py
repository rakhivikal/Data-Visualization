def decide_voter(person_age):
    result = ""
    
    if person_age < 18:
        result = "Not Eligible"
    else:
        result = "Eligible"
    
    return result

# Input
user_age_value = int(input("Enter your age: "))

# Function call
final_result = decide_voter(user_age_value)

# Output
print("Result:", final_result)