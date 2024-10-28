# Programa que pede dois números e fazer uma operação

while escolha == "s": 
   op = input("Qual a operação a utilizar (+ ou s, - ou sub, * ou m, / ou d):")
   n1 = int(input("Introduza um numero"))
   n2 = int(input("Introduza outro numero"))

   if op.lower() in "+s":
       resultado = n1 + n2
   elif op.lower() in "-sub":
       resultado = n1 - n2
   elif op.lower() in "*m":
       resultado = n1 * n2
   elif op.lower() in "/d":
       resultado = n1 / n2
    elif op.lower() == "somatório":
        i1 = int(n1)
        i2 = int(n2)
        resultado = 0
        for i in range(i1,i2):
            resultado = resultado + i         
   else:
       print("Operação não é válida")
       resultado = None

   if resultado is not None:
       print(resultado)

   escolha = input("Pretende continuar a fazer comntas (s/n)? ")
   escolha = escolha.strip().lower()
