def build_even_list(max_limit):
    even_result = []
    current = 1

    while current <= max_limit:
        if current % 2 == 0:
            even_result.insert(len(even_result), current)
        current += 1

    return even_result

# Input
limit_input = int(input("Enter N value: "))

# Function call
final_list = build_even_list(limit_input)

# Output
print("Even numbers from 1 to", limit_input, ":", final_list)