# Central Park Squirrel Data using Pandas

import pandas

file_path =  '/home/argento/Documents/Education/100Days_of_Python/[Day 25:] Working with CSV Data and the Pandas Library/CentralPark_Squirell/'

squirrel_data = pandas.read_csv(f'{file_path}'+'2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

type_of_squirrel = squirrel_data['Primary Fur Color'].unique()

count_gray = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
count_cinnamon = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
count_black = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

print(type_of_squirrel)
print(count_gray)
print(count_cinnamon)
print(count_black)

new_data_dict ={
    'Fur Color' : ['Gray', 'Cinammon','Black'],
    'Count' : [count_gray, count_cinnamon, count_black]
}

new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv(f'{file_path}'+'new_data.csv')

