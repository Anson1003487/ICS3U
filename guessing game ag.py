import random

def main():
    target_number = random.randint(1, 100)
    guess_count = 0
    max_guesses = 6

    print("Hello! Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
    print(f"You have a maximum of {max_guesses} tries.\n")

    while guess_count < max_guesses:
        guess_count += 1
        try:
            user_guess = int(input(f"Guess #{guess_count}: "))
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
            continue

        if user_guess < target_number:
            print("Higher!")
        elif user_guess > target_number:
            print("Lower!")
        else:
            print("You guessed right!")
            return

    print(f"Sorry: you are out of guesses! The answer was {target_number}. Better luck next time!")

if __name__ == "__main__":
    main()

simple 1 :
Hello! Welcome to the number guessing game!
I am thinking of a number between 1 and 100. It is your turn to guess what it is.
You have a maximum of 6 tries.

Guess #1:  5
Higher!
Guess #2:  67
Higher!
Guess #3:  33
Higher!
Guess #4:  78
Lower!
Guess #5:  75
Lower!
Guess #6:  70
You guessed right!

simple 2 :
Hello! Welcome to the number guessing game!
I am thinking of a number between 1 and 100. It is your turn to guess what it is.
You have a maximum of 6 tries.

Guess #1:  5
Higher!
Guess #2:  10
Higher!
Guess #3:  20
Higher!
Guess #4:  30
Higher!
Guess #5:  40
Higher!
Guess #6:  80
Lower!
Sorry: you are out of guesses! The answer was 51. Better luck next time!
