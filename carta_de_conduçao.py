"""
Programa que na carta de condução começa-se com 12 pontos e
vai perdendo pontos dependendo da infração que fez
"""
pontos = 12
infraçao_leve = 0
infraçao_grave = 0
infraçao_mgrave = 0
op = 0
while op !="4":
    print("pontos",pontos)
    if pontos==0:
        print("Perdeu a carta")
    print("1.Muito grave\n2.Grave\n3.Leve\n4.Terminar")
    op=input(":")
    if op=="1":
        pontos = pontos - 6
        infraçao_mgrave = infraçao_mgrave + 1
    if op=="2":
        pontos = pontos - 4
        infraçao_grave = infraçao_grave + 1
    if op=="3":
        if infraçao_leve > 0:
            pontos = pontos - 1
        infraçao_leve = infraçao_leve + 1
    if(infraçao_mgrave ==1 and infraçao_grave ==1) or (infraçao_grave==2):
        pontos = 0    
    if pontos < 0:
        pontos = 0                
        