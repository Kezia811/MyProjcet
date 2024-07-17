# Cosntrua uma página para duas notas escolares 
    # Calcular a média das notas
MÉDIA = (nota1 + nota2) / 2
    
    # Verificar o status do aluno baseado na média
if MÉDIA < 4:
        print("Aluno reprovado")
    elif MÉDIA >= 6:
        print("Aluno aprovado direto")
    elif 4 <= MÉDIA < 6:
        # Se a média estiver entre 4 e 6, verifica a situação na recuperação
        if MÉDIA < 5:
            print("Aluno em recuperação. Reprovado na recuperação.")
        else:
            print("Aluno em recuperação. Aprovado na recuperação.")
    else:
        return "Erro nos dados fornecidos"

# Função principal para executar o programa
 main():
    # Solicita as notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Obtém o status do aluno
    resultado = verificar_status_aluno(nota1, nota2)
    
