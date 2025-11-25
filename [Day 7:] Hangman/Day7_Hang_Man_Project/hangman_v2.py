import random
import os
from hangman_art import stages, logo
from words import word_list

stage_len = len(stages)
guessed_letter = []
underscore = []

def game_start(word):
    os.system('cls')  
    print(logo)
    print('Welcome to HangMan_v1.2\n')
    print('The word is: {} \n'.format(word))
    print(stages[stage_len-1])
    print(f"{' '.join(underscore)}")

def get_new_word():
    chosen_word = random.choice(word_list)
    return chosen_word
#Choosing Random Word.

chosen_word = get_new_word()
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    underscore += '_'

#Menu 

game_start(chosen_word)

#Game Loop


lives = 0
end_game = True

while end_game:
    while lives < stage_len - 1:
        
        #User Guessed letter
        guess = input('\nGuess a letter: ').lower()
        
        #Clear the Screen:
        os.system('cls')  

        #Check if the guessed letter is in the chosen word
        for possition in range(0,word_lenght):
            letter = chosen_word[possition]
            if letter == guess:
                if letter in underscore[possition]:
                    print('You have already chosen: "{}"'.format(letter))
                else: 
                    underscore[possition] = letter
        
        print(f"{' '.join(underscore)}")
        print(stages[stage_len-1-lives])

        if guess in guessed_letter:
            print('You already tried with "{}". Choose a different letter.\n'.format(guess))
            show_letters = input('Would you like to see all the wrong guessed letters? (Y/N)\n').lower()
            if show_letters == 'y':
                print(' '.join(guessed_letter))
        
        elif guess not in underscore:
            os.system('cls')
            print('"{}" is not in the word. You lose a life.'.format(guess))
            lives +=1
            print(stages[stage_len-1-lives])
            guessed_letter.append(guess)
        
        if '_' not in underscore:
            break

    if '_' in underscore:
        print('You Lose')
        print('The word was: "{}"'.format(chosen_word))
        try_again = input ('Would you like to try again?: (Y/N)\n').lower()
        if try_again != 'y':
            end_game = False
        else:
            lives = 0
            chosen_word = get_new_word()
            word_lenght = len(chosen_word)
            underscore.clear()
            guessed_letter.clear()
            for _ in range(word_lenght):
                underscore += '_'
            game_start(chosen_word)
    else:
        print('You won')
        try_again = input ('Would you like to play again?: (Y/N)\n').lower()
        if try_again != 'y':
            end_game = False
        else:
            lives = 0
            chosen_word = get_new_word()
            word_lenght = len(chosen_word)
            underscore.clear()
            guessed_letter.clear()
            for _ in range(word_lenght):
                underscore += '_'
            game_start(chosen_word)