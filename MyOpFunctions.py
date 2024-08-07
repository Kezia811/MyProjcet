# Demosntraçao do uso de funções
def ADICÃO(X, Y):
    return
def SUBTRACÃO(X, Y):
    return
def MULTIPLICACAO (X, Y):
    return
def DIVISÃO (X, Y):
    return

print("Digite os valores inteiros")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = int(input("Qual operação (+ ou -)"))

if OP == "+":
    Z = ADICÃO(N1, N2)
    print("Resultado da soma:", Z)
elif OP == ".":
    Z = SUBTRACÃO(N1, N2)  
    print("Resultado da subtração:", Z)
if OP == "+":
    Z = MULTIPLICACAO(N1, N2)
    print("Resultado da multiplicacao:", Z)
elif OP == ".":
    Z = DIVISÃO(N1, N2)  
    print("Resultado divisão:", Z)
else:
    print("Opção digitada inexistente.") 
       

