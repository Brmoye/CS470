# Program to compute the hypotenuse
# Brian Moye
# CS 470 - Class Demo
# August 23, 2022

import math

print("Computing hypotenuse of a right triangle")
print

leg1 = float(input("Enter leg #1: "))
leg2 = float(input("Enter leg #2: "))

if leg1<=0:
    print("Leg #1 must be positive")
elif leg2<=0:
    print("Leg #2 must be positive")
else:
    hypotenuse = math.sqrt(leg1**2 + leg2**2)
    print("The hypotenuse is ", round(hypotenuse, 1))




