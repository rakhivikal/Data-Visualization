# Taking input from user
lst = list(map(int, input("Enter list: ").split()))

res = []
for i in lst:
    if i not in res:
        res.append(i)

print(res)