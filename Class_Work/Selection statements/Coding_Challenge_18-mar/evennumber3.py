def even_values_generator(n_value):
    numbers = list(range(1, n_value + 1))
    even_nums = []
    
    for item in numbers:
        if not item % 2:   # different way to check even
            even_nums.append(item)
    
    return even_nums

# Input
limit_val = int(input("Enter value of N: "))

# Function call
result_list = even_values_generator(limit_val)

# Output
print("Even numbers are:", result_list)