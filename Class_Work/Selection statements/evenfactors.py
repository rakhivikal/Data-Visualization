# Program to display even factors of a number

# taking input from user
num = int(input("Enter a number: "))

print("Even factors of", num, "are:")

# loop from 1 to num
for i in range(1, num + 1):
    
    # check if i is factor of num
    if num % i == 0:
        
        # check if factor is even
        if i % 2 == 0:
            print(i)