# Demosntração de matrizes em Phyton 
print("Eis, a tabela numérica original")
TABUADA = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
MULTIPLICAR = int(input("Digite o multiplicador:"))

for X in range(0, 3):
    for Y in range(0, 3):
        TABUADA[X][Y] == TABUADA[X][Y] * MULTIPLICAR
                
print("Eis, O multiplicador: ", MULTIPLICAR)
print("Confira o resultado das operações.")
for RESULTADO in TABUADA:
    print(RESULTADO)  