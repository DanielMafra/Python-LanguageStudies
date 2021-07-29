def notas(*args, situacao=False):
    infos = dict()
    maior = menor = soma = media = 0
    infos['total'] = len(args)

    for nota in args:
        if nota == 0:
            maior = nota
        if nota > maior:
            maior = nota
    infos['maior'] = maior

    for nota in args:
        menor = nota
        if nota < menor:
            menor = nota
    infos['menor'] = menor

    for nota in args:
        soma += nota
    infos['media'] = soma/infos['total']

    if situacao:
        if infos['media'] < 6:
            infos['situacao'] = "BAD"
        elif infos['media'] <= 7:
            infos['situacao'] = "GOOD"
        elif infos['media'] >= 9:
            infos['situacao'] = "EXCELLENT"
    else:
        pass
    return infos


resp = notas(5.5, 2.5, 1.5, situacao=True)
print(resp)

# code ref https://github.com/guilherme-learning-center/Curso-Python-Gustavo-Guanabara/blob/master/mundo_3/aula_21/desafio_105.py
