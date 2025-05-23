# Student Name: [Anson Tang]
# Student Number: [1003487]
# Course Code: ICS3U
# Part 1: Even or odd?
# Variable Dictionary:
#   num1: First input number (int)
#   num2: Second input number (int)
#   result: Product of num1 and num2 (int)

# Display welcome message
print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Get user input
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))


# Check even/odd using modulo
if num1 % 2 == 0 or num2 % 2 == 0:
    print(f"The product {num1} x {num2} will be an even number.")
else:
    print(f"The product {num1} x {num2} will be an odd number.")

Part 2 :
# Variable Dictionary:
#   edge: Length of cube edge (float)
#   diagonal: Calculated inner diagonal length (float)

import math

# Get cube edge length
edge = float(input("Please enter the edge length of your cube: "))

# Calculate and print diagonal (edge × √3)
diagonal = edge * math.sqrt(3)

# print the result
print(f"The length of the inner diagonal of a cube with side length {edge} is: {diagonal:.2f}")

Part 3 :
# Variable Dictionary:
#   cents: Input amount in cents (int)
#   quarters: Number of quarters (int)
#   dimes: Number of dimes (int)
#   nickels: Number of nickels (int)
#   pennies: Number of pennies (int)
#   remaining: Remaining cents after each calculation (int)

# Get cents amount (0-99)
cents = int(input("Enter cents (0-99): "))

# Calculate coins
quarters = cents // 25
dimes = (cents % 25) // 10
nickels = (cents % 25 % 10) // 5 
pennies = cents % 5

# Build output string
output = []
if quarters: output.append(f"{quarters} quarter{'s'[:quarters^1]}")
if dimes: output.append(f"{dimes} dime{'s'[:dimes^1]}")
if nickels: output.append(f"{nickels} nickel{'s'[:nickels^1]}")
if pennies: output.append(f"{pennies} penn{'ies'[:pennies^1]}")

# Print result
print(f"{cents} cents = {', '.join(output)}")
