# Nato Alphabet Project

import pandas

file_path = '[Day 26:] List Comprehension and the Nato Alphabet/NATO Alphabet Project'

# Creating a dictionary from the NATO phonetic alphabet CSV file
nato_data = pandas.read_csv(f"{file_path}/"+"nato_phonetic_alphabet.csv")
print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# Creating a list from user input

user_input = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in user_input]

print(nato_list)