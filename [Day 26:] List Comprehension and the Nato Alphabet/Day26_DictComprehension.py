#Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# using if condition
# new_dict = {new_key:new_value for item in list if test}
# using key:value in dict
# new_dict = {new_key:new_value for (key,value) in dict.items()}


#Looping through a list to create a dictionary
import random

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

# creating random scores for each names

students_score = {student:random.randint(1,100) for student in names}
print(students_score)

#Looping through a dict to create a new dict with condition
passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)