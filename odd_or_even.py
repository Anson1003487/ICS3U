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

# Student Name: [Anson Tang]
# Student Number: [1003487]
# Course Code: ICS3U
# Part 2: The inner (or body) diagonal of a cube
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
