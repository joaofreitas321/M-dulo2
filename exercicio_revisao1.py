# Programa para gerir o embarque num avião
total_nomes = 0
lugares = int(input("Introduza o nº de lugares no aviao"))
bilhetes = int(input("Introduza o nº de blihetes vendidos"))

while bilhetes > 0:
    nome = input("Introduza o nome do passageiro")
    total_nomes = total_nomes + nome + '\n'
    bilhetes = bilhetes - 1


if bilhetes > lugares:
   print("O número de bilhetes vendidos não corresponde ao número de lugares")