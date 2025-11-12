
'''
#String Manipulation

print('Hello'[0])
print('Hello'[4])
print('Hello'[-1])
print("123"+"456")

#Large Integers
print(123_456)

#Float Numbers
print(3.14159)

#Basic Math
print(123 + 456)

#Type Errors
len(123456)  # This will raise an error because len() expects a string, list, or other iterable, not an integer.
len("123456") # This works because "123456" is a string.

#String Methods
print("Hello".lower())
print("Hello".upper())
print("Hello".isupper())
print("Hello".isalpha())
print("Hello".count("l"))

#Type Checking
type(123)   # This will return <class 'int'>
type("Hello")  # This will return <class 'str'>
type(3.14)  # This will return <class 'float'>
type(True)  # This will return <class 'bool'>   

#PEMDAS

print(3 + 5 * 2 - (4 / 2) ** 2)     # This will follow the order of operations (PEMDAS) to compute the result.


'''
'''
# BMI Calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
print(int(bmi))

# Alternative rounding method
print(round(bmi))

# f-string formatting
print(f"Your BMI is {bmi:.2f}")

'''

#Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input('What percentage tip would you like to give? 15, 18, or 20? '))
people = int(input("How many people to split the bill? "))

total_to_pay = bill + bill*(tip/100)
total_per_person = total_to_pay / people

print(f"Each person should pay: ${total_per_person:.2f}")



