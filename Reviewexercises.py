# Cadastro 
#  Programa com dados dos clientes.

NOME = input("Digite o nome do cliente: ")
DATA = input("Digite o nascimento: ")
RG = input("Digite o RG: ")
ABERTURA = input("Digite o dia da abertura c/c: ")
FILIAÇÃO = input("Digite o nome dos seus pais.")
SALDO = input("Digite o saldo da sua conta.")

print("O tipo de serviço que quer fazer.")
print("1. Saldo, 2. Depósito, 3. Saque")
SALDO = int(input("Digite uma opção: "))

match SALDO: 
    case 1:
        print("Quer consultar o saldo.")
        
    case 2:
        print("Quer fazer um depósito.")
           
    case 3:
        print("Quer fazer um saque.") 