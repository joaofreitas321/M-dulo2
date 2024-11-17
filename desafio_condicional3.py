# Programa que lê 2 nº e se forem iguais faz a sua soma se não a sua multiplicação
resultado = 0

n1 = int(input("Introduza um numero"))
n2 = int(input("Introduza outro numero"))

if n1 == n2:
    resultado = n1 + n2
else:
    resultado = n1 * n2

print("O resultado é:", resultado)