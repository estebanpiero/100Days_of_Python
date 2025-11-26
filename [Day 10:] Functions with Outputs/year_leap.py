# Year Leap Calculator

def is_leap_year(year):
    """Determine if a given year is a leap year.

    A year is a leap year if it is divisible by 4,
    except for end-of-century years, which must be divisible by 400.

    Args:
        year (int): The year to check.
    
    This is how you work out whether if a particular year is a leap year. 

            - on every year that is divisible by 4 with no remainder
            - except every year that is evenly divisible by 100 with no remainder 
            - unless the year is also divisible by 400 with no remainder   
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = 2020
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


