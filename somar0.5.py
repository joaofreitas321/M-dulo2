# Programa que lê um número e listar os 10 números a seguir somando 0.5
n1 = float(input("Introduza um número"))

n1 = n1 + 0.5
soma = 0

for i in range(10):
    if i < 9:
         print(n1,end=",")
    else:
         print(n1,end=",")
    soma = soma + n1          
    n1 = n1 + 0.5
   
print("=",soma)    