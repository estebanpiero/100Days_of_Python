# Using a dictionary to create a dictionary that takes weather temperature in celsius and converts it to fahrenheit

weather_c = {"Monday": 12, 
             "Tuesday": 14,
             "Wednesday": 15, 
             "Thursday": 14, 
             "Friday": 21, 
             "Saturday": 22, 
             "Sunday": 24}

weather_f = {day:(temperature * 9/5 + 32) for (day,temperature) in weather_c.items()}
print(weather_f)