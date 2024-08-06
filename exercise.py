# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    x = input('Enter a letter: ').upper()
    print(f'The letter {x} is a vowel') if x == ("A" or "E" or "I" or "P" or "U") else print(f'The letter {x} is a consonant')
        
# Call the function
# check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    y = int(input("Please enter your age: "))
    aboveAge = True if y >= 18 else False
    print("You are eligible") if aboveAge else print("You are not eligible")

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    z = int(input("Input a dog's age: "))
    a = (z * 10) if(z <= 2) else (20 + ((z - 2) * 7))
    print(f"The dog's age in dog years is {a}")

# Call the function
# calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    b = input("Is it cold (yes/no) ").lower()
    
    if (b == "yes"):
        b = True

    elif (b == "no"):
        b = False
    else:
        print("Please type yes or no")
        weather_advice()        

    c = input("Is it raining (yes/no) ").lower()

    if (c == "yes"):
        c = True
    elif (c == "no"):
        c = False
    else:
        print("Please type yes or no")
        weather_advice()

    if (b and c):
        print("Wear a waterproof coat.")
    elif (b and not c):
        print("Wear a warm coat.")
    elif (not b and c):
        print("Carry an umbrella.")
    elif (not b and not c):
        print("Wear light clothing.")

# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    d = input("Enter the month of the year (Jan - Dec): ").lower()
    if (d in months):
        mmm = d
    else:
        print("Response not reconginzed. Please try again")
        determine_season()

    e = int(input("Enter the day of the month: "))
    
    if (e in range(1, 31)):
        dd = e
    else:
        print("Response not reconginzed. Please try again")
        determine_season()
    
    match (mmm, dd):
        #      - Dec 21 - Mar 19: Winter
        case (mmm, dd) if mmm == "dec" and dd >= 21:
            season = "Winter"
        case (mmm, dd) if mmm == "jan" and dd or mmm == "feb" and dd:
            season = "Winter"
        case (mmm, dd) if mmm == "mar" and dd <= 19:
            season = "Winter"
        #      - Mar 20 - Jun 20: Spring
        case (mmm, dd) if mmm == "mar" and dd >= 20:
            season = "Spring"
        case (mmm, dd) if mmm == "apr" and dd or mmm == "may" and dd:
            season = "Spring"
        case (mmm, dd) if mmm == "jun" and dd >= 20:
            season = "Spring"
        #      - Jun 21 - Sep 21: Summer
        case (mmm, dd) if mmm == "jun" and dd >= 21:
            season = "Summer"
        case (mmm, dd) if mmm == "jul" and dd or mmm == "aug" and dd:
            season = "Summer"
        case (mmm, dd) if mmm == "sep" and dd >= 21:
            season = "Summer"
        #      - Sep 22 - Dec 20: Fall
        case (mmm, dd) if mmm == "Sep" and dd >= 22:
            season = "Spring"
        case (mmm, dd) if mmm == "oct" and dd or mmm == "nov" and dd:
            season = "Spring"
        case (mmm, dd) if mmm == "dec" and dd >= 20:
            season = "Spring"

    print(f'{mmm} {dd} is in {season}')

# Call the function
# determine_season()

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

import random

def guess_number():
    # Your control flow logic goes here
    n = random.randint(1, 100)
    guess = 0
    while guess in range(5): 
        print(f"Remaining guesses: {5 - guess}")
        guess += 1
        userGuess = int(input("Enter a number within 1 and 100: "))
        while not userGuess in range(1, 101):
            try:
                print("Value not within range.")
                userGuess = int(input("Enter a number within 1 and 100: "))
            except ValueError:
                print("That wasn't an interger")
                userGuess = int(input("Enter a number within 1 and 100: "))
        if userGuess < n:
            print("Guess is too low")
        if userGuess > n:
            print("Guess is too high")
        if guess == 5 and n != userGuess:
            print(f"Sorry, you failed to guess the number in five attempts! The number was {n}!")
        if n == userGuess: 
            print("Congratulations, you guessed correctly!")
            break
    
# Call the function
guess_number()