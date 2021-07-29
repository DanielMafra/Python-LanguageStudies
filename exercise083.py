expr = str(input('Enter the expression: '))
stack = []

for simb in expr:
    if simb == '(':
        stack.append('(')
    elif simb == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('Your expression is valid!')
else:
    print('Your expression is wrong!')
