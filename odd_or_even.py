# Student Name: [Anson Tang]
# Student Number: [1003487]
# Course Code: ICS3U
# Part 1: Even or odd?
# Variable Dictionary:
#   num1: First input number (int)
#   num2: Second input number (int)
#   result: Product of num1 and num2 (int)

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print(f"The product {num1} x {num2} will be an even number.")
else:
    print(f"The product {num1} x {num2} will be an odd number.")
