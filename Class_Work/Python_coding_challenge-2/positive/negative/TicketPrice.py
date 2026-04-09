# Taking day input
day = input("Enter day: ")

# Dictionary storing ticket prices
prices = {
    "Sunday": 200,
    "Monday": 100,
    "Tuesday": 120
}

# Get price using dictionary
print(prices.get(day, "Invalid day"))