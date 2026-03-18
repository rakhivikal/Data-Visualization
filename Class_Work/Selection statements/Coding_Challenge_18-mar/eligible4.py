def check_person_status(age_number):
    flag = False
    
    if age_number >= 18:
        flag = True
    
    if flag:
        return "Eligible"
    else:
        return "Not Eligible"

# Input
input_age = int(input("Enter age of person: "))

# Function call
status_result = check_person_status(input_age)

# Output
print("Eligibility Result:", status_result)