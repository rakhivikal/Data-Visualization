# Taking input from user
lst = list(map(int, input("Enter list: ").split()))

freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print("Frequency =", freq)