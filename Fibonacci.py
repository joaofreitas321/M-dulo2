# Programa que imprime a série de Fibonacci até a um número N fornecido pelo utilizador.
soma = 0
x1 = 0
x2 = 1
n1 = int(input("Quantos nº da sequência pretende"))
print(x1,",",x2)

for i in range (0,n1):
    soma = x1 + x2
    print(soma)
    x1 = x2
    x2 = soma 