# Brian Moye
# August 23, 2022
# CS 470 - Assignment 2
# Asks the user for a maximum value and finds the prime numbers
#   up to that value

maxNum = int(input("Enter maximum value: "))
primes  = [True] * (maxNum - 1)

# 1 isn't a prime so we're just going to start the list from 2,
#   with index 0 representing 2
for number in range(2, (maxNum + 1) // 2):
    for multiple in range(number, maxNum + 1):
        index = (number * multiple)
        if (index > maxNum):
            break
        else:
            primes[index - 2] = False

print("The prime numbers up to ", maxNum, " are: ", sep="", end="")
for i in range(0, maxNum - 1):
    if (primes[i] == True):
        print(i + 2, end=" ")
