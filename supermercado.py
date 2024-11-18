# Programa que pergunta quantas unidades o cliente comprou e calcule o preço total a pagar
unidades = int(input("Introduza o numero de unidades que comprou"))
quantidade = int(input("Introduza a quantidade"))

while unidades <= 10:
    valor = 10
while unidades > 10 and unidades <=20:
    valor = 10 * 0.05 * quantidade
while unidades > 20:
    valor = 10 * 0.20 * quantidade
print(valor)         