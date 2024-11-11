"""
Programa que testa se uma plavra passe é segura. Tem de ter letras,
pelo menos uma maiúscula e uma minuscula, números, pelo menos 8 carateres
e um carater especial: !?@€.,;:-_
"""
alfabetoM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabetom = "abcdefghijklmnopqrstuvwxyz"
numero = "1234567890"
carater_especial = "!?@€.,;:-_"
ter_maiúscula = False
ter_minuscula = False
ter_numero = False
ter_carater_especial = False
password = input("Introduza a sua palavra passe")
for letra in alfabetoM:
    if letra in password:
        ter_maiúscula = True
        break
for letra in alfabetom:
    if letra in password:
        ter_minuscula = True
        break
for letra in numero:
    if letra in password:
        ter_numero = True
        break
for letra in carater_especial:
    if letra in password:
        ter_carater_especial = True
        break                        
if ter_maiúscula == True and ter_minuscula == True and ter_numero == True and ter_carater_especial == True and len(password)>= 8:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")                               