phrase = str(input('Type a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = together[::-1]

print("{}'s reverse is {}.".format(together, reverse))

if reverse == together:
    print('We have a pallidrome!')
else:
    print('The typed sentence is not a palindrome!')
