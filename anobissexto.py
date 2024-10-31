# Programa que diz se é ano bissexto ou não
ano = int(input("Introduza o ano"))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')    