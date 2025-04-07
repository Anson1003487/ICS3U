cents = int(input("Please enter the amount of change in cents: "))
cents = cents % 100

quarters = cents // 25
remaining = cents % 25

dimes = remaining // 10
remaining = remaining % 10

nickels = remaining // 5
pennies = remaining % 5

parts = []
if quarters > 0:
    parts.append(f"{quarters} quarter{'s' if quarters != 1 else ''}")
if dimes > 0:
    parts.append(f"{dimes} dime{'s' if dimes != 1 else ''}")
if nickels > 0:
    parts.append(f"{nickels} nickel{'s' if nickels != 1 else ''}")
if pennies > 0:
    parts.append(f"{pennies} penn{'ies' if pennies != 1 else 'y'}")

print(f"{cents} cents can be {', '.join(parts)}.")
