#Original code to debug
#year = input('Which year do you want to check: ')

#""" if year % 4 == 0:
#    if year % 100 == 0:
#       if year % 400 == 0:
#          print('leap year')
#       else:
#            print('No leap year')
#    else:
#        print('Leap year')
#else:
#   print('No leap year.') """

#Fixed Code

#
# year = int(input('Which year do you want to check: '))

'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = 1900 

if is_leap(year):
    print('Leap year.')
else:
    print('No leap year.')  
'''

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

target = 100
fizz_buzz(target)