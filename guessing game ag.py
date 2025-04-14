
# Student Name: [Anson Tang
# Student Number: [1003487]
# Course Code: ICS3U
# Programming Assignment 2: A number guessing game
# Variable Dictionary:
Variable Dictionary:
#   target: Number to guess (1-100)
#   guess: User's guessed number
import random

# Generate target number
target = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1-100 within 6 attempts\n")

# Attempt 1
guess = int(input("Attempt 1: "))
if guess == target:
    print("Correct! You win!")
else:
    print("Higher!" if guess < target else "Lower!")
    
    # Attempt 2
    guess = int(input("Attempt 2: "))
    if guess == target:
        print("Correct! You win!")
    else:
        print("Higher!" if guess < target else "Lower!")
        
        # Attempt 3
        guess = int(input("Attempt 3: "))
        if guess == target:
            print("Correct! You win!")
        else:
            print("Higher!" if guess < target else "Lower!")
            
            # Attempt 4
            guess = int(input("Attempt 4: "))
            if guess == target:
                print("Correct! You win!")
            else:
                print("Higher!" if guess < target else "Lower!")
                
                # Attempt 5
                guess = int(input("Attempt 5: "))
                if guess == target:
                    print("Correct! You win!")
                else:
                    print("Higher!" if guess < target else "Lower!")
                    
                    # Attempt 6
                    guess = int(input("Attempt 6: "))
                    if guess == target:
                        print("Correct! You win!")
                    else:
                        print(f"Game Over! The number was: {target}")
