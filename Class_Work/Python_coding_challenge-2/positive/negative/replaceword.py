# Taking input from user
s = input("Enter string: ")

res = ""
for ch in s:
    if ch.lower() in "aeiou":
        res += "*"
    else:
        res += ch

print(res)