# Program to convert time given in seconds into hours, minutes, and seconds

# Step 1: Take input from the user in seconds
total_seconds = int(input("Enter time in seconds: "))

# Step 2: Calculate number of hours
# 1 hour = 3600 seconds
hours = total_seconds // 3600

# Step 3: Calculate remaining seconds after hours
remaining_seconds = total_seconds % 3600

# Step 4: Calculate number of minutes from remaining seconds
# 1 minute = 60 seconds
minutes = remaining_seconds // 60

# Step 5: Calculate remaining seconds after minutes
seconds = remaining_seconds % 60

# Step 6: Display the converted time
print("Time in Hours:", hours)
print("Time in Minutes:", minutes)
print("Time in Seconds:", seconds)

# Step 7: Display the result in formatted form
print("Converted Time =", hours, "hours", minutes, "minutes", seconds, "seconds")