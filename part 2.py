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
