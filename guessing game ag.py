
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

# Initialize game variables
target = random.randint(1, 100)  
attempts = 0                     
max_attempts = 6                

# Print game instructions
print("Guess the secret number between 1 and 100")
print(f"You have {max_attempts} attempts to guess correctly.\n")

# Main game loop - runs until max attempts reached
while attempts < max_attempts:
    attempts += 1  
    
# Get and validate user input
    while True:
        try:
            guess = int(input(f"Attempt #{attempts}: ")) 
            if 1 <= guess <= 100:  # Validate range
                break
            print("Please enter a number between 1-100")
        except ValueError:  # Handle non-number input
            print("Invalid input. Please enter a number.")

    # Check guess against target
    if guess == target:
        print(f"\nCongratulations! You guessed the number in {attempts} tries!")
        break  
    elif guess < target:
        print("Go higher!")  
    else:
        print("Go lower!")   

# If loop completes without correct guess
else:  
    print(f"\nGame over! The secret number was {target}.")
    print("Better luck next time!")

# Final message
print("\nThanks for playing the Number Guessing Game!")
    
