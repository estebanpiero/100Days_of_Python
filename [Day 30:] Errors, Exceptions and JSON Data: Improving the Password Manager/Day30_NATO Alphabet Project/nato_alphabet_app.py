# Nato Alphabet Project
# Adding Error Handling

import pandas

file_path = '[Day 26:] List Comprehension and the Nato Alphabet/NATO Alphabet Project'

# Creating a dictionary from the NATO phonetic alphabet CSV file
nato_data = pandas.read_csv(f"{file_path}/"+"nato_phonetic_alphabet.csv")
print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# Creating a list from user input

is_ok = True

while is_ok:
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed. Please try again.")
    else:
        is_ok = False

print(nato_list)