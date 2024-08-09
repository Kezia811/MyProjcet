# Revisão 
print("O que você achou dos nossos serviços.")
print("1. Péssimo, 2. Ruim, 3. Razoável, 4. Bom, 5. Ótimo")
AVALIACAO = int(input("Digite uma opção: "))

match AVALIACAO:
    case 1:
        print("O serviço precisa melhorar muito.")
        print("Avaliação: reprovado!")
    case 2:
        print("O serviço precisa melhorar em alguns quesitos.")
        print("Avaliação: reprovado!")    
    case 3:
        print("Nem bom, nem ruim.")
        print("Avaliação: recuperação!")    
    case 4:
        print("Aceitável no geral, embora possa melhorar.")
        print("Avaliação: Aprovado!")
    case 5:
        print("Perfeito, melhor que isso estraga.")
        print("Avaliação: Aprovado!")   
    case _:
        print("A opção digitada não está correta.")
        print("Obrigada pela atenção!")     