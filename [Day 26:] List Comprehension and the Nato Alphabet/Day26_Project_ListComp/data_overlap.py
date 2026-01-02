# Data overlap between files

files_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 26:] List Comprehension and the Nato Alphabet/Day26_Project'

with open(f'{files_path}/file1.txt') as file1:
    data1 = file1.readlines()
    data1 = [int(item.strip()) for item in data1]

with open(f'{files_path}/file2.txt') as file2:
    data2 = file2.readlines()
    data2 = [int(item.strip()) for item in data2]
overlap = [number for number in data1 if number in data2]

print(overlap)