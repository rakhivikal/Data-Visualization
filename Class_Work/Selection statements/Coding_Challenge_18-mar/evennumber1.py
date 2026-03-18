def generate_even_series(limit_value):
    result_list = []
    num = 2
    
    while num <= limit_value:
        result_list.append(num)
        num += 2
    
    return result_list

# Input
user_input = int(input("Enter the value of N: "))

# Function call
even_result = generate_even_series(user_input)

# Output
print("Even numbers up to", user_input, "are:", even_result)