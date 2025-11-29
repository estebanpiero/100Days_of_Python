#Number Guessing Game

import random

def number_guessing_game():
   
    secret_number = random.randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if level == 'easy':
        max_attempts = 10
    elif level == 'hard':
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to 'easy' mode.")
        max_attempts = 10
    
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    if attempts >= max_attempts and guess != secret_number:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_guessing_game()
# Scope