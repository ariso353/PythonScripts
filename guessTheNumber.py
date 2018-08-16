'''
Randomly generate a number and ask the user to guess
Author: Amanda Riso

******History******
Date      Initials  Description of change
20180816  ANR       Changed checkIfValid to include .isdigit() check. Added
                    variables to for beginning and end of range. Changed invalid
                    prompt. Added intGuess to convert userGuess after checkIfValid
                    returns true.
20180814  ANR       Initial Script
'''

import random

beginRange = 1
endRange = 20


def generateRandomNumber():
    return random.randint(beginRange, endRange)


def promptUser():
    return input("Guess a number between 1 and 20: ")


def checkIfValid(userInput):
    if userInput.isdigit() and beginRange <= int(userInput) <= endRange:
        return True
    else:
        return False


def main():
    randomNumber = generateRandomNumber()
    promptAgain = True

    while(promptAgain):
        userGuess = promptUser()

        if checkIfValid(userGuess):
            intGuess = int(userGuess)
            if intGuess == randomNumber:
                print("You guessed right!")
                promptAgain = False
            elif intGuess > randomNumber:
                print("Your guess was too high!")
                promptAgain = True
            else:
                print("Your guess was too low!")
                promptAgain = True
        else:
            print("That was not a valid entry. Try again")
            promptAgain = True


if __name__ == "__main__":
    main()
