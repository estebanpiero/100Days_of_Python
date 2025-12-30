# Mail Merger Project
# This script merges data from txt file with a list of names

letter_file_path = "/home/argento/Documents/Education/100Days_of_Python/[Day 24:] Files, Directories and Paths/Day24Project_MailMerger/Inputs/Letters/starting_letter.txt"
names_file_path = "/home/argento/Documents/Education/100Days_of_Python/[Day 24:] Files, Directories and Paths/Day24Project_MailMerger/Inputs/Names/invited_names.txt"
output_directory = "/home/argento/Documents/Education/100Days_of_Python/[Day 24:] Files, Directories and Paths/Day24Project_MailMerger/Outputs/ReadyToSend/"

#-----------------------------------------------
# Read the letter template and name list
#-----------------------------------------------

with open(letter_file_path, "r") as letter_file:
    letter_template = letter_file.read()

with open(names_file_path, "r") as names_file:
    names_list = names_file.readlines()

invitation_list = [name.strip() for name in names_list]

for name in invitation_list:
    personalized_letter = letter_template.replace("[name]", name)
    
    # Create a personalized letter file for each name
    
    with open(f"{output_directory}letter_for_{name}.txt", "w") as output_file:
        output_file.write(personalized_letter)
    print(f"Created letter for {name} at f'./{output_directory}letter_for_{name}.txt'")

