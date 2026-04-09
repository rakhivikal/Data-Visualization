# Taking input from user
lst = list(map(int, input("Enter numbers: ").split()))

unique = []
for i in lst:
    if i not in unique:
        unique.append(i)

print("Unique count =", len(unique))