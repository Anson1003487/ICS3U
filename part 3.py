cents = int(input("Please enter the amount of change in cents: "))
cents = cents % 100  

quarters = cents // 25
remaining = cents % 25

dimes = remaining // 10
remaining = remaining % 10

nickels = remaining // 5
pennies = remaining % 5

output = []
if quarters > 0:
    output.append(f"{quarters} quarter{'s' if quarters > 1 else ''}")
if dimes > 0:
    output.append(f"{dimes} dime{'s' if dimes > 1 else ''}")
if nickels > 0:
    output.append(f"{nickels} nickel{'s' if nickels > 1 else ''}")
if pennies > 0:
    output.append(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

if output:
    print("Your change is: " + ", ".join(output) + ".")
else:
    print("No change needed.")

example:
Please enter the amount of change in cents:  41
Your change is: 1 quarter, 1 dime, 1 nickel, 1 penny.
