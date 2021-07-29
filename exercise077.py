words = ('learn', 'program', 'language', 'python', 'course', 'free of charge',
         'studying', 'practice', 'work', 'marketplace', 'programmer', 'future')

for w in words:
    print(f'\nIn the word {w.upper()} we have: ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
