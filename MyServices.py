# Minhas atribuições
EXECUÇÃO = input("O serviço foi feito (sim/não)? ")
AVALIAÇÃO = int(input("Qual a not da avaliação (1/5)? "))

if EXECUÇÃO == "sim" and AVALIAÇÃO == 1:
    print("O serviço foi péssimo")
elif EXECUÇÃO == "sim" and AVALIAÇÃO ==2:
    print("O serviço foi ruim")
elif EXECUÇÃO == "sim" and AVALIAÇÃO == 3:
    print("O serviço foi razoável")    
elif EXECUÇÃO == "sim" and AVALIAÇÃO == 4:
    print("O serviço foi bom")      
elif EXECUÇÃO == "sim" and AVALIAÇÃO == 5:
    print("O serviço foi excelente")        
else:
    if EXECUÇÃO == "não" and AVALIAÇÃO == 0:
       RECLAMAÇÃO == input("Digite a sua reclamação") 
    else:
        print("As duas valiações não fazem sentido")  