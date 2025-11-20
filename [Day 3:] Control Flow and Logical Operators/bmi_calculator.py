print('Welcome to the BMI calculator!')
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = round(weight / (height**2))

print('Your BMI is: {:.2f}'.format(bmi))

if bmi < 18.5:
    print('You are underweight.')
elif bmi < 24.9:
        print('Your weight is normal.')
elif bmi < 29.9:
    print('You are overweight.')
else:
    print('You are too fat!')

