# Program to calculate Simple Interest with data validation

# Taking input for Principal amount
P = float(input("Enter the Principal amount: "))

# Validate Principal (should not be negative)
if P <= 0:
    print("Principal amount must be greater than 0")

else:
    # Taking input for Rate of Interest
    R = float(input("Enter the Rate of Interest (in %): "))
    
    # Validate Rate
    if R <= 0:
        print("Rate of interest must be greater than 0")
    
    else:
        # Taking input for Time
        T = float(input("Enter the Time (in years): "))
        
        # Validate Time
        if T <= 0:
            print("Time must be greater than 0")
        
        else:
            # Formula of Simple Interest
            SI = (P * R * T) / 100
            
            # Display result
            print("Simple Interest is:", SI)