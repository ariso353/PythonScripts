'''
Randomly generate a number and ask the user to guess
Author: Amanda Riso

******History******
Date      Initials  Description of change
--------  --------  -----------------------------------------------------------
20180816  ANR       Changed isValidGuess to include .isdigit() check.
                    Added variables to for beginning and end of range and
                    modified the prompt to use the new variables. Changed
                    invalid guess print. Removed checking guess to a checkGuess
                    method. Added Comments.
20180814  ANR       Initial Script
'''

import random


strtRng = 1
endRng = 20


# Generates random number between given range.
def generateRandomNumber():
    return random.randint(strtRng, endRng)


# Ask the user to guess a number between a range.
def promptUser():
    return input("Guess a number between {} and {} :".format(strtRng, endRng))


# Check if the guess entered is a number and if it is between the range.
def isValidGuess(userInput):
    if userInput.isdigit() and strtRng <= int(userInput) <= endRng:
        return True
    else:
        return False


# Checks if the user's guess is correct or not
def checkGuess(guess, randomNumber):
    if guess == randomNumber:
        print("You guessed right!")
        return False
    elif guess > randomNumber:
        print("Your guess was too high!")
        return True
    else:
        print("Your guess was too low!")
        return True


def main():
    randomNumber = generateRandomNumber()
    promptAgain = True

    while(promptAgain):
        userGuess = promptUser()

        if isValidGuess(userGuess):
            promptAgain = checkGuess(int(userGuess), randomNumber)
        else:
            print("That was not a valid entry. Try again")
            promptAgain = True


if __name__ == "__main__":
    main()
