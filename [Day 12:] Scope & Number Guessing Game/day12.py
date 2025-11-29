#Scope

# Local vs Global Scope

def my_function():
    x = 10  # Local variable
    print("Inside function, x =", x)    
my_function()
# print("Outside function, x =", x)  # This would raise an error    

# Global variable
y = 20

def another_function():
    print("Inside function, y =", y)    
another_function()
print("Outside function, y =", y)   


# Is Prime Function

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True