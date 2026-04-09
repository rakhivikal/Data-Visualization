# Taking input from user
s = input("Enter sentence: ")

words = s.split()
count = 0

for i in words:
    count += 1

print("Words =", count)