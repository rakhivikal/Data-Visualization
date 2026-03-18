def print_even_numbers(limit):
    even_list = []
    for num in range(1, limit + 1):
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Input
n = int(input("Enter N: "))

# Function call
result = print_even_numbers(n)

# Output
print("Even numbers between 1 to", n, "are:", result)