# Taking input from user
s = input("Enter sentence: ").split()

longest = s[0]
for word in s:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)