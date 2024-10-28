# Programa que vai indicar o peso e o orçamento do utilizador

orçamento = float(input("Introduza o seu orçamento:"))
peso = float(input("Introduza a capacidade do peso a carregar:"))

while orçamento > 0 and peso > 0:
    preço = float(input("Indique o preço do produto comprado:"))
    peso_produto = float(input("Indique o peso do produto comprado:"))
if preço == 0:
    break
if orçamento < preço or peso < prso_produto:
    print("Não tem dinheiro ou produto muito pesado")
else:
    orçamento 