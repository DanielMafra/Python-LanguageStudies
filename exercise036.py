house = float(input('House value: U$'))
salary = float(input("Buyer's salary: U$"))
years = int(input('How many years of financing? '))
installments = house / (years * 12)
minimum = (salary * 30) / 100

print('To pay for a U${:.2f} house in {} years'.format(
    house, years), end='')
print(' the installment will be U${:.2f}'.format(installments))

if installments <= minimum:
    print('Loan can be granted!')
else:
    print('Loan denied!')
