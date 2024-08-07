# Demosntração do uso de funções 
def MENOR():
    print("Eis os programas ideais para você.")
    print("Pica Pau, To & Jerry, Chaves")
    print("Se passar das 22h, vai dormir.")
    return
def MAIOR():
    print("Eis boas opções de carro para comprar.")
    print("Logan,HRV, Hb20, Compass, Reneggade")
    print("Se beber, não dirija.")
    return

print("Digite a sua idade ")
IDADE = int(input())

if IDADE <18:
    MENOR()
else:
    MAIOR()    