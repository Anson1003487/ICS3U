# Student Name: [Anson Tang]
# Student Number: [1003487]
# Course Code: ICS3U
# Part 3: Making change in coins
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
