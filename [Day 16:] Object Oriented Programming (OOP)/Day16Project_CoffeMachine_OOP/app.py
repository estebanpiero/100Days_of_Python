from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
table = PrettyTable()

is_on = True


table.field_names = ["Coffee", "Price"]

for items in menu.get_items().split("/")[:-1]:
    drink = menu.find_drink(items)
    table.add_row([drink.name, f"${drink.cost}"])



while is_on:
    print("Welcome to the Coffee Machine!")
    print("Here is the menu:")
    print(table)
    user_drink = input(f"What would you like to drink?: ")

    if user_drink == "off":
        is_on = False
    elif user_drink == "report":
        coffee_maker.report()
        money_machine.report() 
    else:
        # Find the drink object by its name
        drink = menu.find_drink(user_drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


