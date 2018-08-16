'''
Simulates a dice roll
Author: Amanda Riso

******History******
Date      Initials  Description of change
--------  --------  -----------------------------------------------------------
20180814  ANR       Initial Script

'''
import random


# Rolls the dice between 1 - 6
def printRoll():
    print(random.randint(1, 6))


# Asks the user if they would like to roll the dice
def promptUser():
    return input("Would you like to roll the dice? (y/n)")


# Tests if the user would like to roll and then calls the printRoll function
def main():
    while promptUser().lower() == 'y':
        printRoll()


# Runs the main funtion
if __name__ == "__main__":
    main()
