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
def print_roll():
    print(random.randint(1, 6))


# Asks the user if they would like to roll the dice
def prompt_user():
    return input("Would you like to roll the dice? (y/n)")


# Tests if the user would like to roll and then calls the print_roll function
def main():
    while prompt_user().lower() == 'y':
        print_roll()


# Runs the main funtion
if __name__ == "__main__":
    main()
