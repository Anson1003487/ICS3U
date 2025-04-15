# Student Name: [Anson Tang]
# Student Number: [1003487]
# Course Code: ICS3U
# Programming Assignment 3: Palindrome Checker
# Variable Dictionary:
#   words: List of words to check (palindromes and non-palindromes)
#   word: Current word being checked
#   is_palindrome: Flag indicating if the word is a palindrome
#   max_index: Midpoint index for character comparison
#   i: Loop index for character comparison

# Define an array containing up to 10 words (mix of palindromes and non-palindromes)
words = ["racecar","noon","desk","civic","radar","level","school","rotor","refer","madam"]

# Iterate through each word in the list
for word in words:
    is_palindrome = True  # Flag to track palindrome status
    max_index = len(word) // 2  # Calculate midpoint for comparison
    
    # Compare characters from both ends towards the center using a for loop
    for i in range(max_index):
        # Check front character (i) vs back character (-1 - i)
        if word[i] != word[-1 - i]:
            is_palindrome = False  # Mismatch found
    
    # Determine and print the result
    if is_palindrome:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

# Program termination message
print("Goodbye!")
