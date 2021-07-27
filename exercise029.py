velocity = float(input("What is the car's current speed? "))

if velocity > 80:
    print('FINED! You have exceeded the allowed limit which is 80km/h')
    mulct = (velocity - 80) * 7
    print('You must pay a U${} fine!'.format(mulct))

print('Have a nice day! Drive safely!')
