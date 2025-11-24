import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

score = 0
total_games = 0

replay = True
game_images = [rock, paper, scissors]

def user_choice_input():
    while True:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice < 0 or user_choice >= 3:
            user_continue_or_leave = input("You typed an invalid number. Press 'Q' to leave or 'Enter' to try again.").lower()
            if user_continue_or_leave == 'q':
                break   
            continue
        else:
            print(game_images[user_choice])
            break
    return user_choice

def computer_choice_generate():
    computer_choise = random.randint(0,len(game_images)-1)
    print("Computer chose: {}".format(game_images[computer_choise]))
    return computer_choise

def determine_winner(user_choice, computer_choise):
    global total_games
    total_games += 1
    if user_choice == computer_choise:
        print("It's a draw")
    elif (user_choice == 0 and computer_choise == 2) or (user_choice == 1 and computer_choise == 0) or (user_choice == 2 and computer_choise == 1):
        print("You win!")
        global score
        score += 1  
    else:
        print("You lose")

while replay == True:
    user_selection = user_choice_input()
    determine_winner(user_selection, computer_choice_generate())
    user_replay_choice = input("Do you want to play again? Type 'Y' for Yes or 'N' for No: ").lower()
    if user_replay_choice == 'y':
        replay = True
    else:
        replay = False
        print("Thanks for playing!")    

print("Your played a total of {} games and your score is: {}".format(total_games, score))

