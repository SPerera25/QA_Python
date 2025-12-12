'''
num = int(input("Enter a number: "))

if ( num % 2 == 0 ) :
    print("Number, " + str(num) + ", is Even")
else :
    print("Number, " + str(num) + ", is Odd")

'''


#In case user enter a non-interger value:

try:
    num = int(input("Enter a number: "))

    if ( num % 2 == 0 ) :
        print("Number, ", num, " is Even")
    else :
        print("Number, ", num, " is Odd")

except ValueError:

    print("Invalid input! Please enter an integer value.")