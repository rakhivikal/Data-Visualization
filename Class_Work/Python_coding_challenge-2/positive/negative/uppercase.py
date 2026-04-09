# Taking input from user
s = input("Enter string: ")

res = ""
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch) - 32)
    else:
        res += ch

print(res)