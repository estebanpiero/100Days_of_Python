#HANGMAN Project

import random
import os

from words import word_list
from hangman_art import stages, logo

underscore = []
attempts = len(stages) - 1 


def selecting_word():
    chosen_word = random.choice(word_list)
    return chosen_word

def starting_game():
    print(logo)
    print(stages[6])


def game_logic(chosen_word, attempts, underscore):
    for _ in chosen_word:
        underscore += "_"
    print(" ".join(underscore) + "\n")

    while attempts > 0:
        user_guess = input("Guess a letter: ").lower()
        if user_guess in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == user_guess:
                    underscore[position] = user_guess
                    # print(" ".join(underscore))
        else:
            attempts -= 1
        os.system("clear")
        print(stages[attempts])
        print(" ".join(underscore))
        
        if attempts == 0:
            print("You lose.")
            print(f"The word was: {chosen_word}")

        elif "_" not in underscore:
            print("You win.")

chosen_word = selecting_word()
starting_game()
game_logic(chosen_word, attempts, underscore)




    

