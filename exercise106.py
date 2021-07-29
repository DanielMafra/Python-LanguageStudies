from time import sleep


def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)


def pyhelp(comando):
    help(comando)


def default_loop():
    while True:
        escreva("Helper system PyHELP")
        funcao_ou_lib = input("Function or Lib > ")

        if funcao_ou_lib[0].lower() == "f":
            break
        else:
            pyhelp(funcao_ou_lib)


default_loop()

# code ref https://github.com/guilherme-learning-center/Curso-Python-Gustavo-Guanabara/blob/master/mundo_3/aula_21/desafio_106.py
