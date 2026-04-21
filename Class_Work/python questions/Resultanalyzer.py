# Reading student data from file
try:
    file = open("students.txt", "r")

    topper = ("", 0)  # (name, percentage)

    for line in file:
        try:
            # Split data
            data = line.strip().split(",")

            id = data[0]
            name = data[1]
            m1 = int(data[2])
            m2 = int(data[3])
            m3 = int(data[4])

            total = m1 + m2 + m3
            percentage = total / 3

            # Grade assignment
            if percentage >= 90:
                grade = "A"
            elif percentage >= 75:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            else:
                grade = "Fail"

            print(name, "Total:", total, "Percentage:", percentage, "Grade:", grade)

            # Find topper
            if percentage > topper[1]:
                topper = (name, percentage)

        except:
            print("Invalid data found, skipping...")

    print("\nTopper:", topper[0], "with", topper[1], "%")

    file.close()

except:
    print("File not found")