# Taking username and password input
username = input("Enter username: ")
password = input("Enter password: ")

# Checking credentials
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")