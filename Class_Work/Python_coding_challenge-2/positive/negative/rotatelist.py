# Taking input from user
lst = list(map(int, input("Enter list: ").split()))

rotated = [lst[-1]] + lst[:-1]

print("Rotated list =", rotated)