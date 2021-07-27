weight = float(input('How much do you weigh? (kg) '))
height = float(input('What is your height? (m) '))
bmi = weight / (height ** 2)

print('Your BMI is {:.1f}'.format(bmi))

if bmi < 18.5:
    print('You are underweight')
elif 18.5 <= bmi < 25:
    print('You are in the normal weight range')
elif 25 <= bmi < 30:
    print('You are overweight')
elif 30 <= bmi < 40:
    print('You are obese')
elif bmi >= 40:
    print('You are morbidly obese, beware!')
