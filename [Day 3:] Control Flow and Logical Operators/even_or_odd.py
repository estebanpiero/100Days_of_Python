number = int (input('Which number do you want to check if even or odd?'))

repeat = True

while repeat != False:
        
    if number % 2 == 0:
        print('{} is an EVEN number.'.format(number))
    else:
        print('{} is an ODD number.'.format(number))

    try_again = input('Do you want to try again? Type Yes or No: ').lower()
    
    if try_again == 'yes':
        number = int (input('Which number do you want to check if even or odd?'))
    else:
        print('Thank you for using the Even or Odd checker. Goodbye!')
        repeat = False
        break

