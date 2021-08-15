# Simple Calculator
x = float(input('Enter a Number: '))
y = float(input('Enter another Number: '))
z = int(input('Please enter a number, 1 for Addition, 2 for Subtraction, 3 for Division, and 4 for Multiplication: '))
tuples = ('Please Enter a Different Number',x + y, x - y, x / y, x * y,'Please Enter a Different Number')
print(tuples[z])