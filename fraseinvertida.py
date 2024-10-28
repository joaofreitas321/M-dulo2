# Programa que lê uma frase e mostra uma letra por linha por ordem inversa
frase = input("Introduza uma frase:")

for posicao in range (len(frase)-1,-1,-1):
    print(frase[posicao])
    