# File System to Open/Read/Write/Delete files and directories

#--------------------------------------------------------------
# Opening and Reading a File
#--------------------------------------------------------------

file_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 24:] Files, Directories and Paths/my_file.txt'


'''
file = open(file_path, 'r') # Open a file in read mode
content = file.read()          # Read the content of the file
print(content)                 # Print the content
file.close()                  # Close the file


with open(file_path, 'r') as file:  # Using 'with' to open a file
    content = file.read()           # Read the content of the file
    print(content)                  # Print the content
'''

#--------------------------------------------------------------
# Opening and Writing on a File
#--------------------------------------------------------------

'''

with open(file_path, 'a') as file:  # Open a file in append mode
    file.write('\nNew line added to the file.')  # Write a new line to the file

'''
#--------------------------------------------------------------
# Deleting a File
#--------------------------------------------------------------

# os.remove(file_path)  # Uncomment this line to delete the file
# Be cautious while using os.remove() as it will permanently delete the file

#--------------------------------------------------------------
# Understanding Relative and Absolute Paths
#--------------------------------------------------------------

# Absolute Path: The complete path from the root directory to the file
absolute_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 24:] Files, Directories and Paths/my_file.txt'
# Relative Path: The path relative to the current working directory
relative_path = 'my_file.txt'  # Assuming the current working directory is the one containing the file

with open(relative_path, 'r') as file:  # Using 'with' to open a file
    content = file.read()           # Read the content of the file
    print(content)                  # Print the content

# You can use os.getcwd() to get the current working directory
current_working_directory = os.getcwd()
print(f'Current Working Directory: {current_working_directory}')