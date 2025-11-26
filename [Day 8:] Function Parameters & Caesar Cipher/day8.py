#Functions and Inputs

#def greet():
#    print("Hello!")
#    print("How are you?")
#    print("I'm fine, thanks!")
#    print("Goodbye!")
#
#greet()

# Function that allows inputs

# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"How are you {name}?")
# 
# greet_with_name("Alice")

# Life is Weeks

#def life_in_weeks(age):
#    weeks_left = (90 - age) * 52
#    print(f"You have {weeks_left} weeks left.")
#
#age = int(input("Enter your age: "))
#life_in_weeks(age)


# Function with multiple inputs

#def greet_with_name_and_location(name, location):
#    print(f"Hello {name}!")
#    print(f"How are you {name}?")
#    print(f"Are you in {location}?")
#
#greet_with_name_and_location("Alice", "New York")
#greet_with_name_and_location(name="Alice", location="New York")

# True Love Calculator


def calculate_love_score(name1 , name2):
    true_counter = 0
    love_counter = 0
    combined_name = name1 + name2
    for n in combined_name:
        if n in "true":
            true_counter+=1
        if n in "love":
            love_counter+=1
    return print(f"{true_counter}"+f"{love_counter}")


calculate_love_score(name1=("Kanye West").lower(), name2=("Kim Kardashian").lower())    