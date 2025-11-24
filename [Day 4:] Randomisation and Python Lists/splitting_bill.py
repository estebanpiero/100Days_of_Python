'''
# Splitting Bill

def split_bill(bill_amount, number_of_people):
    """Splits the bill amount among the number of people and returns the amount each person should pay."""
    if number_of_people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return round(bill_amount / number_of_people, 2) 

# Example usage:
bill = float(input("Enter the total bill amount: $"))
people = int(input("Enter the number of people to split the bill: "))
amount_per_person = split_bill(bill, people)
print(f"Each person should pay: ${amount_per_person}")

'''

#Random Person Pays

import random   
def random_person_pays(names):
    """Selects a random person from the list to pay the bill."""
    return random.choice(names)

# Example usage:    
names_list = input("Enter the names of the people, separated by commas: ").split(", ")
payer = random_person_pays(names_list)
print(f"{payer} is going to pay the bill!") 

