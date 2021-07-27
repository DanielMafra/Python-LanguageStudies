phrase = str(input('Type a phrase: ')).upper().strip()

print('The letter A appears {} times in the sentence.'.format(phrase.count('A')))
print('The first letter A appeared at position {}.'.format(phrase.find('A') + 1))
print('The last letter A appeared in position {}.'.format(phrase.rfind('A') + 1))
