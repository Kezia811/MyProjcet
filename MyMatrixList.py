#Demonstração de matrizes em Phyton
TABUADA = []

for x in range (0, 10):
    LINHAS = []
    for y in range (0, 10):
        LINHAS.append(x * y)
    TABUADA.append(LINHAS)

for TABELA in TABUADA:
    print(TABELA)

