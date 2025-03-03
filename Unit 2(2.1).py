prdit: No matter which answer I pick it will just give me one answer "I preety chetties"

modify 1:
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if ch == "A":
    print("I prefer apples")
elif ch == "B":
    print("I prefer bananas")
elif ch == "C":
    print("I prefer cherries")
else:
    print("Invalid choice! Please choose A, B, or C.")
example:
Make a choice from the following menu: 
A: apples
B: bananas
C: cherries
Your choice:  d
Invalid choice! Please choose A, B, or C.

Modify 2: Working with compound conditionals
score = int(input("Enter your score (1-100): "))
if (score >= 80) and (score <= 100):
    print("A")
elif (score >= 70) and (score <= 79):
    print("B")
elif (score >= 60) and (score <= 69):
    print("C")
elif (score >= 50) and (score <= 59):
    print("D")
elif (score >= 0) and (score < 50):
    print("F")
else:
    print("Invalid score! Please enter a number between 1 and 100.")

example:
Enter your score (1-100):  80
A
