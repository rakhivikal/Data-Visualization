import numpy as np

num = 12
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

arr = np.array(factors)
print(arr)