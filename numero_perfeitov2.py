# Programa que lê um número e diz se é perfeito ou não.
numero = int(input("Introduza o limite máximo:"))

for k in range(1,numero):
    soma = 0
    for i in range(1,k):
        resto = k % i
        if resto == 0:
            soma = soma + i

    if soma == k:
        print(f"Numero {k} é perfeito")
    else:
        print(f"Numero {k} não é perfeito. A soma dos seus divisores foi",soma)   
 