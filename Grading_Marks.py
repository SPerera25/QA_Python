
try:
    
    marks = float(input("Enter the marks obtained: "))

    if (marks>=75):
        grade = 'A'  # This is a string variable to hold the grade

    elif (marks>=51):
        grade = 'B'

    elif (marks>=41):
        grade = 'C'

    elif (marks>=31):
        grade = 'D'

    else:
        grade = 'E'

    print("The grade is:", grade)

except ValueError:

    print("Invalid input! Please enter numeric marks.")