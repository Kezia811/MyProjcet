#  Programa com dados dos clientes.

NOME = input("Digite o nome do cliente: ")
DATA = input("Digite o nascimento: ")
RG = input("Digite o RG: ")
ABERTURA = input("Digite o dia da abertura c/c: ")
FILIAÇÃO = input("Digite o nome dos seus pais.")
SALDO = input("Digite o saldo da sua conta.")

if SALDO > 0:
    print("Saldo positivo.")
elif SALDO < 0:
    print("Saldo negativo.")
else:
    print("Sua conta está zerada.")    

    