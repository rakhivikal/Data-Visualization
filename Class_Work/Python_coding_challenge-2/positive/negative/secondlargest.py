# Taking input from user
lst = list(map(int, input("Enter numbers: ").split()))

largest = second = -99999

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)