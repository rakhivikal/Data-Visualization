# Taking input from user
a = set(map(int, input("Enter set1: ").split()))
b = set(map(int, input("Enter set2: ").split()))

result = a.intersection(b)

print("Intersection =", result)