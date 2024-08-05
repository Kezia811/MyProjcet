# Demonstração de multiplicação
def exibir_tabuada(numero):
    print(f"\nTabuada de {numero}")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:3}")

def main():
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        exibir_tabuada(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")