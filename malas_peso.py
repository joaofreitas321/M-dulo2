"""
Programa que lê o peso das malas e quando o limite de carga de carga for atingido indicar que se atingiu
mostrando de seguida o valor apurado em taxas.
"""
peso_porao = 1000 

peso_malas = float(input("Introduza o peso das malas"))
if peso_malas == peso_porao:
    print("Chegou à carga máxima")
elif peso_malas < peso_porao:
    print("Não chegou à carga máxima") 
elif peso_malas > peso_porao:
    print("Excedeu a carga máxima")