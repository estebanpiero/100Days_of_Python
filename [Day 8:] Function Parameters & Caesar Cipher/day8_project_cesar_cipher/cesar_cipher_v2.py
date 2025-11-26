from logo import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

def caesar(method,plain_text,num_shift):
    text = ''
    for char in plain_text:
        possition = alphabet.index(char)
        if method == 'encode':
            new_possition = possition + num_shift
            if new_possition >= len(alphabet):
                over_possition = new_possition - len(alphabet)
                new_char = alphabet[over_possition]
                text += new_char
            else:
                new_char = alphabet[new_possition]
                text += new_char
        elif method == 'decode':
            new_possition = possition - num_shift
            if new_possition < 0:
                over_possition = new_possition + len(alphabet)
                new_char = alphabet[over_possition]
                text += new_char
            else:
                new_char = alphabet[new_possition]
                text += new_char
        else:
            return print('That is not a valid Method.')

    return print(f'The new message is: {text}')

def program_menu():
    os.system('cls')  
    print(logo)
    print('Welcome to the Caesar Cipher Program')
    print('-'*36)
    direction = input('\nType "Encode" to encrypt, type "Decode" to decrypt: \n').lower()
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number: \n'))
    caesar(direction,text,shift)

end_program = True

while end_program == True:
    program_menu()
    cont_prog = input('Would you like to run the program again: (Yes or Y)/(No or N): \n').lower()
    if cont_prog == 'yes' or cont_prog == 'y':
        end_program = True
    elif cont_prog == 'no' or cont_prog == 'n':
        end_program = False 
        print("\n---------------------- Goodbye --------------------------")
    else:
        print('That is not a valid option')
