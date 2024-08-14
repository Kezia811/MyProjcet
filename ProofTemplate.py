# Demsntração do gabarito 
GABARITO = ['B', 'C', 'A', 'E', 'D']

# Inicializando a lista para as respostas do usuário
respostas_usuario = []

# Solicitando as respostas do usuário
print("Insira as respostas para cada questão (use A, B, C, D, E):")
for i in range(1, 6):
    resposta = input(f"Resposta da questão {i}: ").strip().upper()
    while resposta not in ['A', 'B', 'C', 'D', 'E']:
        print("Resposta inválida. Por favor, insira uma resposta válida (A, B, C, D, E).")
        resposta = input(f"Resposta da questão {i}: ").strip().upper()
    respostas_usuario.append(resposta)

# Verificando a quantidade de acertos
acertos = 0
for i in range(len(GABARITO)):
    if respostas_usuario[i] == GABARITO[i]:
        acertos += 1

# Exibindo o resultado
print(f"Você acertou {acertos} questão(ões).")