# Programa que lê um número e diz se é perfeito ou não.
n1 = int(input("Introduza um numero"))
soma = 0

for i in range(1,n1):
    resto = n1 % i
    if resto == 0:
        soma = soma + i

if soma == n1:
    print("É um numero perfeito")
else:
    print("Não é um numero perfeito. A soma dos seus divisores foi",soma)    