def get_even(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result

# Taking input from user
nums = list(map(int, input("Enter list: ").split()))

print("Even numbers =", get_even(nums))