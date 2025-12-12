# Get the square of a number from user input and print the result.

# Function
def square(num):
    return num ** 2

num = float(input("Enter a number to find its square: "))

result = square(num)
print("The square of", num, "is", result)

'''
We can aslo do this without a function:

1.
num = float(input("Enter a number to find its square: "))   
result = num ** 2
print("The square of", num, "is", result)

2.
num = float(input("Enter a number to find its square: "))
print("The square of", num, "is", num ** 2)

3.
num = float(input("Enter a number to find its square: "))
print(f"The square of {num} is {num ** 2}")

4.
num = float(input("Enter a number to find its square: "))
square = lambda x: x ** 2
print("The square of", num, "is", square(num))

    'lambda' creates a small anonymous function.
    x is the input parameter.
    x ** 2 means “x squared.”
    You assign the lambda to a variable called square,so it behaves like a normal function.

'''