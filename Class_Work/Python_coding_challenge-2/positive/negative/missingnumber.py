# Taking input from user
lst = list(map(int, input("Enter numbers: ").split()))

n = len(lst) + 1
expected_sum = n * (n + 1) // 2

missing = expected_sum - sum(lst)

print("Missing number =", missing)