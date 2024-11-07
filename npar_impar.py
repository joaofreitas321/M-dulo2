"""
Programa que solicita ao usuário um número inteiro positivo e imprime a sequência de Collatz
até chegar em 1. A sequência funciona da seguinte forma:
Se o número é par, divida-o por 2.
Se o número é ímpar, multiplique-o por 3 e some 1.
"""
n1 = int(input("Introduza um numero inteiro positivo"))

while n1 != 1:
    resto = n1 % 2
    if resto == 0:
        n1 = n1 // 2
    else:
        n1 = n1 * 3 + 1
    print(n1)        
    
        
