#How to create a list using List comprehension

# list comprehension syntax
# new_list = [new_item for item in list]
# using if condition
# new_list = [new_item for item in list if test]

number = [1,2,3,4,5]
new_list = [n+1 for n in number]
print(new_list)

name = "Angela"
new_list2 = [letter for letter in name]
print(new_list2)

new_range = [num*2 for num in range(1,5)]
print(new_range)

#Conditional List Comprehension
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) <5]
print(short_names)

upper_case_names = [name.upper() for name in names if len(name) >5]
print(upper_case_names)