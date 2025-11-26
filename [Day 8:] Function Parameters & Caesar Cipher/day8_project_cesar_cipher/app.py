# Project Cesar Cipher

from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

def caesar_cipher(method, text, shift):
    if method == "encode":
        encoded_text = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                # new_index = (index + shift) % 26
                new_index = index + shift

                if new_index >= len(alphabet):
                    over_index = new_index - len(alphabet)
                    encoded_text += alphabet[over_index]
                else:
                    encoded_text += alphabet[new_index]
            else:
                encoded_text += char
        return encoded_text

    elif method == "decode":
        decoded_text = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = index - shift
                if new_index < 0:
                    under_index = new_index + len(alphabet)
                    decoded_text += alphabet[under_index]
                else:
                    decoded_text += alphabet[new_index]
            else:
                decoded_text += char
        return decoded_text

def cesar_app():
    print(logo)
    print('-'*36)
    while True:
        method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if method == "encode" or method == "decode":
            result = caesar_cipher(method, text, shift)
            print(f"Here's the result: {result}")
        else:
            print("Invalid method. Please try again.")

cesar_app()