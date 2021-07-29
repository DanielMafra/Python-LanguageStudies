from random import randint
from time import sleep


def sorter():
    numbers = list()
    for n in range(0, 5):
        numbers.append(randint(0, 99))
    print(f" {len(numbers)} values list: ", end="")
    for i in numbers:
        print(f"{i} ", end="")
        sleep(0.5)
    return numbers


def soma_par(lista_numeros):
    pares = list()
    for n in lista_numeros:
        if n % 2 == 0:
            pares.append(n)
    print(f"\nValues is: ", end="")
    print(f"{pares}", end="")
    print(f"\nSum is: {sum(pares)}")


soma_par(sorter())
