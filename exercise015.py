days = int(input('How many days rented? '))
km = float(input('How many km traveled? '))
paid = (days * 60) + (km * 0.15)

print('The total amount to be paid is U${}.'.format(paid))
