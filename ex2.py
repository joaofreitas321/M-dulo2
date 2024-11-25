capacidade = int(input("Qual a capacidade do depósito (litros)?"))
if capacidade >= 100 and capacidade <=1000:
    total_gasto = 0
    for i in range(1,11):
        valor_gasto = int(input(f"{i}ª rega:"))
        if total_gasto + valor_gasto > capacidade:
            break
        total_gasto += valor_gasto
    print("Total gasto:",total_gasto)
    print("Sobra no depóstito:",capacidade-total_gasto)
else:
    print("Capacidade do depósito não é válida")    