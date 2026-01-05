# Catching Error and Exception in Python
'''
try:    
    something that might cause an error

except SomeErrorAs e:
    handle the error

else:
    do this if there is no error

finally:
    do this no matter what
    '''


# FileNotFound Erro

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}. The file does not exist.")

# KeyError

my_dict = {'name': 'Alice', 'age': 30}
try:
    print(my_dict['address'])
except KeyError as e:
    print(f"Error: {e}. The key does not exist in the dictionary.")

# -----------------------------------
# Raise your own Exception

hight =  float(input("Height: "))
weight = float(input("Weight: "))



if hight > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / hight ** 2

print(f"Your BMI is: {bmi}")


