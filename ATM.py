"""
ATM
1- Ver o saldo
2- Depositar o dinheiro
3- Levantar o dinheiro
4- Terminar
"""
saldo = 0
escolha = None 
opção = int(input("Introduza o numero que quer"))
while opção != 4 or saldo < 0:
    print("ATM\n1. Ver Saldo\n2.Depositar\n3.Levantar\n4.Terminar")
    if opção == 1 and saldo >= 0:
        print("Ver o saldo")
    elif opção == 2:
        valor = float(input("Introduza o valor a depositar"))
        d = valor -round(valor,2)
        if d != 0:
            print("O valor não é válido, só pode ter 2 casas decimais")
            continue
        if valor <= 0.01 or valor > 10000:
            print("O valor não é válido")
        else:
             saldo = saldo + valor
             print("O seu saldo atualmente é de", saldo)
    elif opção == 3 and saldo >= 0:
        levantar = float(input("Introduza o dinheiro a levantar"))
        if levantar < 10 or levantar > 400:
            print("O valor não é válido")
        else:
            saldo = saldo - levantar
            print("O seu saldo atualmente é de", saldo)                   