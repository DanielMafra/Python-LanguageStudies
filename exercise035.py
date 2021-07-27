print('-=' * 20)
print('Triangle Analyzer')
print('-=' * 20)

s1 = float(input('First segment: '))
s2 = float(input('Second segment: '))
s3 = float(input('Third segment: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('The above segments can form a triangle!')
else:
    print('The above segments cannot form a triangle!')
