# Programa que cria uma palavra passe segura
import random
A_M = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = ""
A_m = "abcdefghijklmnopqrstuvwxyz"
A_numero = "1234567890"
A_simbolo = "!?@€.,;:-_"

for i in range(2):
    pos = random.randint(0,len(A_M))
    password = password + A_M[pos]

for i in range(2):
    pos = random.randint(0,len(A_m))
    password = password + A_m[pos]

for i in range(2):
    pos = random.randint(0,len(A_numero))
    password = password + A_numero[pos]

for i in range(2):
    pos = random.randint(0,len(A_simbolo))
    password = password + A_simbolo[pos]        