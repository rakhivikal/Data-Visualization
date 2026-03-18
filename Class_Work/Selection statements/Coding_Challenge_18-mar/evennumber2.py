def collect_even(limit_num):
    even_values = []
    
    for value in range(limit_num + 1):
        if value % 2 != 1:
            if value != 0:
                even_values = even_values + [value]
    
    return even_values

# Input
number_input = int(input("Enter the limit: "))

# Function call
even_output = collect_even(number_input)

# Output
print("List of even numbers:", even_output)