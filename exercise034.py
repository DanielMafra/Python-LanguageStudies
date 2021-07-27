salary = float(input("What is the employee's salary? U$"))

if salary <= 1250:
    new = salary + (salary * 15 / 100)
else:
    new = salary + (salary * 10 / 100)

print('Whoever earned U${:.2f} now earns U${:.2f}'.format(salary, new))
