
# Student Name: [Anson Tang
# Student Number: [1003487]
# Course Code: ICS3U
# Programming Assignment 2: A number guessing game
# Variable Dictionary:
#   target: The random number to guess (int)
#   guess: User's current guess (int)
#   attempts: Number of guesses used (int)
#   max_attempts: Maximum allowed guesses (int)

import random

target = random.randint(1, 100)
attempts = 0
max_attempts = 6

print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
print(f"You have a maximum of {max_attempts} tries.\n")

while attempts < max_attempts:
    attempts += 1
    guess = int(input(f"Guess #{attempts}: "))
    
    if guess == target:
        print("\nYou Guessed right!")
        break
    elif guess < target:
        print("Higher!")
    else:
        print("Lower!")

if attempts == max_attempts and guess != target:
    print(f"\nSorry: you are out of guesses! The answer was {target}. Better luck next time!")

    
