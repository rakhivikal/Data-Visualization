def fetch_even_numbers(limit_value):
    even_set = set()
    
    for num in range(2, limit_value + 1, 2):
        even_set.add(num)
    
    return sorted(even_set)

# Input
limit_input_value = int(input("Enter N: "))

# Function call
even_numbers_result = fetch_even_numbers(limit_input_value)

# Output
print("Even numbers list:", even_numbers_result)