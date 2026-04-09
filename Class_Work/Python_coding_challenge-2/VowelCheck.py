# Taking character input
ch = input("Enter character: ")

# Convert to lowercase and check in vowel list
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not Vowel")