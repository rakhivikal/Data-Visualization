def calculate_bonus(salary):
    bonus = salary * 0.07
    return bonus

salary = int(input("Enter salary: "))
print("Bonus =", calculate_bonus(salary))