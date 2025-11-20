print('Welcome to Pizza Delivery')
print('Small Pizza = $15')
print('Medium Pizza = $20')
print('Large Pizza = $25')
print('Add Pepperoni for Small = $2')
print('Add Pepperoni for Medium and Large = $3')
print('Extra Chesse = $1')
print(' ')

orders = 0
bill = 0
repeat = True

def pizza_order(bill):

    size = input('What size pizza do you want? S, M, or L: ')
    pepperoni = input('Do you want pepperoni? Y or N: ')
    extra_cheese = input('Do you want extra cheese? Y or N: ')

    if size == 'S':
        bill += 15
    elif size == 'M':
        bill += 20
    else:
        bill += 25

    if pepperoni == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3
    if extra_cheese == 'Y':
        bill += 1   
    return bill
    
    
while repeat != False:
    bill = pizza_order(bill) 
    orders += 1
       
    option = input('Do you want to order another pizza? Y or N: ')

    if option.upper() == 'N':
        print('Thank you for your order!')
        break

print(f'Your final bill for a total amount of {orders} is: ${bill}.')
