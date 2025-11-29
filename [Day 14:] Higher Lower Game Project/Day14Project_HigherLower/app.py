# Day 14 Project: Higher Lower Game Project
#

from random import choice

from art import logo, vs
from game_data import data

# Initialize game variables
amount_of_data = len(data)
score = 0
game_should_continue = True
account_a = choice(data)
account_b = choice(data)

def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_followers(a_followers, b_followers):
    """Checks if the user's guess is correct."""
    if a_followers > b_followers:
        return 'a'
    else:
        return 'b'

print(logo)

while game_should_continue:
    account_a = account_b
    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    
    correct_answer = check_followers(a_follower_count, b_follower_count)

    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")