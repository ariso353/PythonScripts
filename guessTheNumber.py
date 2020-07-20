'''
Randomly generate a number and ask the user to guess
Author: Amanda Riso

******History******
Date      Initials  Description of change
--------  --------  -----------------------------------------------------------
20180816  ANR       Changed is_valid_guess to include .isdigit() check.
                    Added variables to for beginning and end of range and
                    modified the prompt to use the new variables. Changed
                    invalid guess print. Removed checking guess to a check_guess
                    method. Added Comments.
20180814  ANR       Initial Script
'''

import random


strtRng = 1
endRng = 20


# Generates random number between given range.
def generate_random_number():
    return random.randint(strtRng, endRng)


# Ask the user to guess a number between a range.
def prompt_user():
    return input("Guess a number between {} and {} :".format(strtRng, endRng))


# Check if the guess entered is a number and if it is between the range.
def is_valid_guess(user_input):
    if user_input.isdigit() and strtRng <= int(user_input) <= endRng:
        return True
    else:
        return False


# Checks if the user's guess is correct or not
def check_guess(guess, random_number):
    if guess == random_number:
        print("You guessed right!")
        return False
    elif guess > random_number:
        print("Your guess was too high!")
        return True
    else:
        print("Your guess was too low!")
        return True


def main():
    random_number = generate_random_number()
    prompt_again = True

    while(prompt_again):
        user_guess = prompt_user()

        if is_valid_guess(user_guess):
            prompt_again = check_guess(int(user_guess), random_number)
        else:
            print("That was not a valid entry. Try again")
            prompt_again = True


if __name__ == "__main__":
    main()
