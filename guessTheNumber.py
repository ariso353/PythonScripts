'''
Randomly generate a number and ask the user to guess
Author: Amanda Riso

******History******
Date      Initials  Description of change
20180814  ANR       Initial Script
'''

import random


def generateRandomNumber():
    return random.randint(1, 20)


def promptUser():
    return input("Guess a number between 1 and 20!")


def checkIfNumber(userInput):
    if type(userInput) is int:
        return True
    else:
        return False


def main():
    randomNumber = generateRandomNumber()
    promptAgain = True

    while(promptAgain):
        userGuess = promptUser()

        if checkIfNumber(userGuess):
            if userGuess == randomNumber:
                print("You guessed right!")
                promptAgain = False
                break
            elif userGuess > randomNumber:
                print("Your guess was too high!")
                promptAgain = True
                break
            else:
                print("Your guess was too low!")
                promptAgain = True
                break
        else:
            print("You did not enter a real number.  Try again")
            promptAgain = True


if __name__ == "__main__":
    main()
