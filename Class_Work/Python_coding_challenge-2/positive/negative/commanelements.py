# Taking input from user
a = list(map(int, input("Enter list1: ").split()))
b = list(map(int, input("Enter list2: ").split()))

common = []
for i in a:
    if i in b and i not in common:
        common.append(i)

print(common)