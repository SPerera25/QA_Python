''' Calculate employee salary after applying several updates using
assignment operators.
The base salary is $50,000.
The employee gets a 10% raise, then a $2000 bonus,
then a $1500 deduction for taxes. Print the final salary. '''

salary = 50000
salary += salary * (10/100)  # 10% raise
salary += 2000               # $2000 bonus
salary -= 1500               # $1500 deduction for taxes

print("The final salary is: $", salary)