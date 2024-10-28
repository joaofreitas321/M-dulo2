# Programa que vai inserir 5 números superiores a 10 e inferiores a 100 e contá-los
contar = 0

while contar < 5:
    n1 = int(input("Introduza um número maior que 10 e menor que 100"))
    if n1 > 10 and n1 < 100:
        contar = contar + 1
    
print(contar)    

