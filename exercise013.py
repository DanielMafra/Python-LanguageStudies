salary = float(input("What is the employee's salary? U$"))
new = salary + (salary * 15 / 100)

print('An employee who earned U${:.2f}, with increase 15%, starts to receive U${:.2f}.'.format(
    salary, new))
