# Month abbreviation to number mapping
month_dict = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
    'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

# Arrays to store data
date_numbers = []
words = []

# Read and process data file
with open('wordle.dat') as file:
    for line in file:
        month_abbr, day, year, word = line.strip().split()
        # Convert date to YYYYMMDD format
        date_int = int(year + month_dict[month_abbr] + day)
        date_numbers.append(date_int)
        words.append(word.upper())  # Store words in uppercase

# Main program
print("Welcome to the Wordle Database!")
user_choice = input("Enter w if you're looking for a word, or d for a date: ").lower()

# Word search functionality
if user_choice == 'w':
    target_word = input("What word are you looking for? ").upper()
    found = False
    
    # Linear search through words list
    for idx in range(len(words)):
        if words[idx] == target_word:
            print(f"The word {target_word} was the solution to the puzzle on {date_numbers[idx]}")
            found = True
            break
    
    if not found:
        print(f"{target_word} was not found in the database.")

# Date search functionality
elif user_choice == 'd':
    input_year = input("Enter the year: ")
    input_month = input("Enter the month (3-letter abbreviation): ").capitalize()
    input_day = input("Enter the day: ").zfill(2)  # Pad with leading zero if needed
    
    # Validate month input
    if input_month not in month_dict:
        print("Invalid month abbreviation.")
    else:
        # Create date integer
        search_date = int(input_year + month_dict[input_month] + input_day)
        
        # Validate date range
        if search_date < 20210619:
            print(f"{search_date} is too early. No Wordles occurred before 20210619.")
        elif search_date > 20240421:
            print(f"{search_date} is too recent. Our records only go as late as 20240421.")
        else:
            # Search for date in database
            date_found = False
            for idx in range(len(date_numbers)):
                if date_numbers[idx] == search_date:
                    print(f"The word entered on {search_date} was {words[idx]}.")
                    date_found = True
                    break
            if not date_found:
                print(f"No word found for the date {search_date}.")

# Exit message
print("Goodbye!")


