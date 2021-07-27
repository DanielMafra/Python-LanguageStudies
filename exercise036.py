house = float(input('Valor da casa: U$'))
salary = float(input('Salário do comprador: U$'))
years = int(input('Quantos anos de financiamento? '))
installments = house / (years * 12)
minimum = (salary * 30) / 100

print('Para pagar uma casa de U${:.2f} em {} anos'.format(
    house, years), end='')
print(' a prestação será de U${:.2f}'.format(installments))

if installments <= minimum:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')
