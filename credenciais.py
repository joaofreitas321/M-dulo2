""" 
Programa que lê as credenciais e tem três tentativas para acertar.
O programa deve terminar se o login falhar ou com o login corretos.
"""
tentativas = 3

while tentativas > 0:
    email = input("Introduza o email")
    password = input("Introduza a password")
    if email == "joaquim@gamil.com" and password == "1234567":
        print("Login efetuado com sucesso")
        break
    tentativas = tentativas - 1
    if email != "joaquim@gmail.com" and password != "1234567":
        print("Login falhou")
    elif email != "joaquim@gmail.com":
        print("Email incorreto")
    else:
        print("Password incorreta")
    if tentativas == 0:
        print("Esgotou as 3 tentativas de login, tente novamente mais tarde")                 