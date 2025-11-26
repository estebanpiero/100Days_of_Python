############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = [] 
end_game = False


def game_results(user_cards, computer_cards):
    print(f"Your final cards: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final cards: {computer_cards}, final score: {sum(computer_cards)}")

def game_calculation(user_cards, computer_cardsy):
    
    if sum(user_cards) == 21:
            print("Blackjack! You win!")
            return
    
    elif sum(user_cards) > 21: 
        for card in user_cards:
            if card == 11:
                user_cards.remove(card)
                user_cards.append(1)
                break
    else:
        while sum(user_cards) < 21:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(random.choice(cards))
                if sum(user_cards) > 21: 
                    for card in user_cards:
                        if card == 11:
                            user_cards.remove(card)
                            user_cards.append(1)
                            
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            else:
                break

        if sum(user_cards) > 21:
            for card in user_cards:
                if card == 11:
                    user_cards.remove(card)
                    user_cards.append(1)
                    break
            print("You went over 21. You lose!")
            game_results(user_cards, computer_cards)
            return

        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
       

        if sum(computer_cards) > 21 or sum(user_cards) > sum(computer_cards):
            print("You win!")
            game_results(user_cards, computer_cards)
            return

        elif sum(user_cards) < sum(computer_cards):
            print("You lose!")
            game_results(user_cards, computer_cards)    
            return
        else:
            print("It's a draw!")
            game_results(user_cards, computer_cards)
            return  


while not end_game:
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_start == 'n':
        end_game = True
        print("Thanks for playing!")
    else:   
        os.system('clear')
        print(logo)
        for i in range(2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: [{computer_cards[0]}] [ ]")
       
        game_calculation(user_cards, computer_cards)
        user_cards.clear()            
        computer_cards.clear()
        


        