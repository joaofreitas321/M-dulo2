# Programa que pede a idade ao utilizador e determina a que classe pertence Ex.: <10 - infantis
idade = int(input("Introduza a idade do jogador"))

if idade < 10:
    print("O jogador pertence à classe dos infantis")
elif idade >= 10 and idade < 14:
    print("O jogador pertence à classe dos iniciados")
elif idade >= 14 and idade < 18:
    print("O jogador pertence à classe dos juniores")
elif idade >= 18:
    print("O jogador pertence à classe dos seniores")
      