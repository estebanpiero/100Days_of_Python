# Reading CSV Files

file_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 25:] Working with CSV Data and the Pandas Library/'

import os
import csv
import pandas

# with open(f'{file_path}'+'/weather_data.csv', 'r') as weather_data:
#     # data = weather_data.readlines()
#     # print(data)
# 
#     data = csv.reader(weather_data)
#     
#     #get the temperature values from csv file
#     temperature = []
# 
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv(f'{file_path}'+'/weather_data.csv')
# print(data)
# print(data['temp'])

#Converting data to dictionary

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data['temp'].mean())

print(data.day)
print(data.condition)

# Get data from a Row the day with the highest temperature

# max_temp = data['temp'].max()
print(data[data.temp == data.temp.max()])

monday = data[data.day=="Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)



# Creating Data Frame from 0



