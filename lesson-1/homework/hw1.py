#1

import math
a = float(input("Enter the number (a): "))
P = 4*a
S = a**2
print(f"The P and S of {a} is: {P} and {S}")

#2

import math
diameter = float(input('Enter the deameter of the circle'))
circuference = math.pi * diameter 
print(f"The circuference of the circle is: {circuference:.2f}")

#3

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
mean = (a + b)/2
print(f"The mean of {a} {b} is: {mean}")

#4

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

sum_ab = a + b
product_ab = a * b 
square_a = a**2
square_b = b**2
print(f"Sum of {a} and {b} is: {sum_ab}")
print(f"product of {a} and {b} is: {product_ab}")
print(f'square of {a} is: {square_a}')
print(f'square of {a} is: {square_b}')
