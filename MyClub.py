# Tabela Campeonato Brasileiro 

CLUBE = input("Digite o nome do clube: ")
POSIÇÃO = int(input("Digite a sua posição: "))

if POSIÇÃO == 1:
    print("Campeão") 
elif POSIÇÃO > 1 and POSIÇÃO <= 6:
    print("Libertadores")
elif POSIÇÃO > 6 and POSIÇÃO <= 12:
    print("Sul-Americana")
elif POSIÇÃO > 12 and POSIÇÃO <= 16:
    print("Sem classificação")    
elif POSIÇÃO > 17 and POSIÇÃO <= 20:
    print("Rebaixado")    
else:
    print("Digite a posição correta")