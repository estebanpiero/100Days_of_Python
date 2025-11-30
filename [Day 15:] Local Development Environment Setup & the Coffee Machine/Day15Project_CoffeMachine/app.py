# Coffe Machine Project

from resources import MENU , resources, money
from art import COFFEE_MACHINE_LOGO

import os   


leftover_resources = resources.copy()

def coffe_machine(user_input):
        
        # Check resources sufficient?
        if user_input in MENU:
            
            drink = MENU[user_input]
            ingredients = drink["ingredients"]
            
            # Get cost of the coffee
            coffee_cost = MENU[user_input]["cost"]
        
            # Check if resources are sufficient
            for item in ingredients:
                if ingredients[item] > leftover_resources[item]:
                    print(f"Sorry there is not enough {item}.")
                    return False
                        
            # Process coins and check transaction successful?
            user_payment = process_coins()

            if user_payment > coffee_cost:
                change = round(user_payment - coffee_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")

                # Update resources and money
                update_resources_and_money(MENU[user_input])
                print(f"Here is your {user_input}. Enjoy!")


        elif user_input == "report":
            coffee_machine_report()
            return True
    
        elif user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            return False
    
        else:
            print("Invalid selection.")
            return False




def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_inserted = quarters + dimes + nickels + pennies
    return total_inserted

def coffee_machine_report():
    print(f"Water: {leftover_resources['water']}ml")
    print(f"Milk: {leftover_resources['milk']}ml")
    print(f"Coffee: {leftover_resources['coffee']}g")
    print(f"Money: ${money['value']}")



def update_resources_and_money(drink):
    money["value"] += drink["cost"]
    ingredients = drink["ingredients"]
    
    for item in ingredients:
        leftover_resources[item] -= ingredients[item]


    


# Main program

continue_program = True

while continue_program != False:
    #os.system("clear")

    print("\nWelcome to the Coffee Machine!")


    # Printing Menu

    print("Menu:")
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Coffee", "Logo"]
    

    for item in MENU:
        cost = MENU[item]["cost"]
        table.add_row([f"{item.capitalize()}: ${cost}", COFFEE_MACHINE_LOGO[item]])
        #print(f"{item.capitalize()}: ${cost}")
        #print(COFFEE_MACHINE_LOGO[item])
    
    print(table)
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    continue_program = coffe_machine(user_input)

    

