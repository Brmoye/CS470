# Brian Moye
# August 23, 2022
# CS 470 - Assignment 2
# Asks the user how many random numbers in the range 0-999 should
#   be generated

import random

numberOfNumbers = int(input("How many numbers [0...999] should be generated (Powers of 10 preferred)? "))
randList = []
beginNine = 0
beginFive = 0
endNine = 0
endFive = 0

for i in range(0, numberOfNumbers):
    num = random.randint(0, 999)
    #randList.append(num)
    firstDigit = int(str(num)[0])
    
    if num % 10 == 5:
         endFive += 1
    elif num % 10 == 9:
        endNine += 1
    if firstDigit == 5:
        beginFive += 1
    elif firstDigit == 9:
        beginNine += 1

print("\nRandomly generated numbers:")
#print(randList, "\n")
print("Numbers beginning with 5: ", beginFive)
print("Numbers beginning with 9: ", beginNine)
print("Numbers ending with 5: ", endFive)
print("Numbers ending with 9: ", endNine)