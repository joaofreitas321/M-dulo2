# Programa que pergunta quantas unidades o cliente comprou e calcule o preço total a pagar
preco_unitario = 10
preco_total = 0
unidades = 0

unidades_compradas = int(input("Quantas unidades comprou"))

while unidades_compradas < unidades:
    unidades_compradas = unidades_compradas + 1

    if unidades_compradas <= 10:
        preco_total = preco_total + preco_unitario
    elif unidades_compradas <= 20:
        preco_total = preco_total + preco_unitario * 0.95
    else:
        preco_total = preco_total + preco_unitario * 0.90
