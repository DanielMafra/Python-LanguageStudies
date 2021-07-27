distance = float(input('How far is your trip? '))
price = distance * 0.50 if distance <= 200 else distance * 0.45

print('You are about to start a {}km journey.'.format(distance))
print('Your ticket will cost U${:.2f}'.format(price))
