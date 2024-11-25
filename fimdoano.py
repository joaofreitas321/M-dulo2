#Programa que insere uma data e temos de saber quantos dias faltam para o fim do ano
dia = int(input("Introduza o dia"))
mês = int(input("Introduza o mês"))
ano = int(input("Introduza o ano"))
mês_atual = 0
soma = 0

for mês in range(mês_atual,13):
    dias_mês = 31
    
    if mês == 4 or mês == 6 or mês == 9 or mês == 11:
        dias_mês = 30
    elif mês == 2:
         if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
             dias_mês = 29
         else:
             dias_mês = 28

faltam = dias_mês - dia
dia = 0
soma = soma + faltam

print("Faltam",faltam,"dias para o fim do ano")
