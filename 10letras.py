"""
Programa que lê 10 letras, uma de cada vez e antes de terminar
deve indicar quantas vogais o utilizador introduziu.
"""

contar = 0
for i in range(10):
    letra = input("Introduza uma letra")
    if letra in "aeiouAEIOU":
        contar = contar + 1
print(contar)        
