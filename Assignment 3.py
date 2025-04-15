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

# Process each word in the array
for word in words:
    is_palindrome = True  # Initialize palindrome flag
    max_index = len(word) // 2  # Calculate midpoint for comparisons
    
    i = 0
    # Compare characters from both ends toward the center
    while i < max_index and is_palindrome:
        # Check front character (i) vs back character (-1 - i)
        if word[i] != word[-1 - i]:
            is_palindrome = False  # Mismatch found
        i += 1  # Move to next character pair
    
    # Display result using ternary operator
    result = "a palindrome" if is_palindrome else "not a palindrome"
    print(f"{word} is {result}")

# Print termination message
print("Goodbye!")
