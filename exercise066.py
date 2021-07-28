sum = cont = 0

while True:
    num = int(input('Enter a value (999 to stop): '))
    if num == 999:
        break
    cont += 1
    sum += num

print(f'The sum of the {cont} values was {sum}!')
