# Brian Moye
# August 31, 2022
# CS 470 - Assignment 4
# A simple dice game

import random

# Initialize/reset the state of the game
def init(numDice):
    totalScore = 0
    dice = [0] * numDice
    return (dice, totalScore)

# Play the game
def game(dice, totalScore):
    status = False
    while(status == False and input("Roll the dice (Y/N)? ").strip().lower() == "y"):
        (dice, totalScore) = roll(dice, totalScore)
        status = gameover(dice)
        display(dice, totalScore, status)
        if (status == True):
            (dice, totalScore) = roll(dice, totalScore)
            display(dice, totalScore, status)
    if (status == False):
        print()
        print("YOU WIN. YOUR SCORE IS:", totalScore)
    
# Display the dice, score, and win/lose status
def display(dice, totalScore, gameStatus):
    print()
    for die in range(1, len(dice) + 1):
        print("Die #{0}".format(die), sep="", end=" ")
    print("  Sum")
    for i in range(0, len(dice)):
        if (i > 9):
            print("%7s"%dice[i], end=" ")
        else:
            print("%6s"%dice[i], end=" ")
    if (gameStatus == True):
        print("=> YOU LOSE!")
    else:
        if (len(dice) > 9):
            print("%6d"%totalScore)
        else:
            print("%5d"%totalScore)

# Generate new numbers for the dice
def roll(dice, totalScore):
    for i in range(0, len(dice)):
        if (dice[i] != 3 and dice[i] != "STUCK"):
            dice[i] = random.randint(1, 6)
        else:
            dice[i] = "STUCK"
    totalScore += sum([x for x in dice if x != 3 and x != "STUCK"])
    return (dice, totalScore)

# Check the game state
def gameover(dice):
    status = True
    for die in dice:
        if (die != 3 and die != "STUCK"):
            status = False
            break
    return status

# Run the program
def main():
    play = "y"
    while(play == "y"):
        numDice = int(input("How many dice in this game? "))
        (dice, totalScore) = init(numDice)
        
        game(dice, totalScore)
        play = input("Play another game (Y/N)? ").strip().lower()
    
main()