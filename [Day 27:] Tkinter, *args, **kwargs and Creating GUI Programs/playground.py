#*arg
# Unlimited positional arguments

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

# print(add(1, 2, 3, 4, 5))  # Returns 1

#**kwargs
# Unlimited keyword arguments

def calculate(n,**kwargs):
    #for key, value in kwargs.items():
    #    print(f"{key}: {value}")
    
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=5, multiply=10)

# Class creation with **kwargs

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Toyota", model="Corolla")
print(my_car.make)  # Outputs: Toyota
print(my_car.model)  # Outputs: Corolla
