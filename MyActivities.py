# Demosntração em operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã?")
print("dormir/estudar/planejar")
MANHÃ = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHÃ or not TARDE:
    print("Você precisa dizer o que vai fazer!")
else:
    if MANHÃ == "dormir"or TARDE == "jogar":
        print("Você está desperdiçando o seu dia!")    
    elif MANHÃ == "estudar" or TARDE == "treinar":
        print("Que bom você irá se aperfeiçoar")
    elif MANHÃ == "planejar" and TARDE == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinamos estas ações ")    

print("Tenha um bom dia!")        
