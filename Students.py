 # Calcular a média dos alunos 
NOTA1 = float(input("Digite a primeira nota: "))
NOTA2 = float(input("Digite a segunda nota: "))
MÉDIA = (NOTA1 + NOTA2) / 2

if MÉDIA >= 6:
    print(("Aprovado."))    
elif MÉDIA < 4:
    print("Aluno reprovado.")
else:
    print("Aluno em recuperação.")

    NOTA3 = float(input("Digite a nota da recuperação: "))
    if NOTA3 >=5:
        print("Aprovado na recuperação.")
    if NOTA3 < 5:
        print("Reprovado na recuperação.")          