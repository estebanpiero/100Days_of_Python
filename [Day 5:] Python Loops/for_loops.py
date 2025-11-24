# Write your code below this line 
# 👇
'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

'''

# Write your code below this line 
# 👇
'''
for number in range(1, 11):
    print(number)   
''' 

# Students Hight 

from numpy import average

print("Welcome to the average height calculator!")
print("Please enter the heights in cm separated by commas, Example: 170, 180, 165.")

students_height = input("Input a list of student heights in cm: \n").split(',')

for n in range(0, len(students_height)):    
    students_height[n] = int(students_height[n])

print(students_height)  

average_height = sum(students_height) / len(students_height)
print(f"The average height is {round(average_height)} cm")

