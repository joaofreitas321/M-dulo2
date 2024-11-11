"""
Programa que pede ao utilizador para inserir três lados e verifica se forma um triângulo válido.
Se não formar dá erro, mas se der indentificamos o tipo de triângulo:
Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes
"""
a = float(input("Introduza o valor do lado a"))
b = float(input("Introduza o valor do lado b"))
c = float(input("Introduza o valor do lado c"))

if a <= 0 or b <= 0 or c <= 0 or a+b < c or a+c < b or b+c < a:
    print("Não é um triângulo válido")
else:    
    if a == b and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")      