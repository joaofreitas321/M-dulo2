# aprendizagens M02
 
# existem 3 tipops de variáveis:
n=int(input("insira um número inteiro"))
n1=float(input("insira um número real"))
n2=str(input("insira uma frase/letra/palavra"))
 
#condições
#se  eu tiver 18 ou mais de idade sou adulto
idade=int(input("insira a sua idade"))
if idade>= 18:
  print("é adulto")
else:
  print("Ainda não é adulto")
 
  #ciclo for
    #usado quando quremos repetir uma ação  determinado n de vezes
for i in range(10,1,1):
    print("olá")
 #ciclo while
  # usado para repetir uma ação enquanto uma condição se verificar
unidades=int(input("insira o número de unidades que comprou"))
quantidade=int(input("insira a quantidade"))
while unidades<=10:
 valor=10
 while unidades>10 and unidades<=20:
  valor=10*0.05*quantidade
  while unidades>20:
   valor=10*0.20* quantidade
print(valor)
 
#  Strings
# multiplicar strings faz juntar 2 letras ou palavras
N1=afonso
N=pedrão
# resultado-afonsopedrão
 
# a função LEN lê o tamanho das strings
# a função BREAK para o programa
# a função CONTINUE é uasda para o ciclo voltar ao ínicio
 
""" sinais de operações
/ -divisão
* -multiplicação
% -resto da divisão
// -divisão inteira
<= - menor ou igual
>= - maior ou igual
!= - diferente
== - comparação
"""