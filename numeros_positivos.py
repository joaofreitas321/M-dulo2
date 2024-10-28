"""
Progrma que imprime todos os números positivos menores de 100 
com excecão dos números que são múltiplos do número 3.
"""

for i in range (1,100):
    if i % 3 != 0:
        print(i)