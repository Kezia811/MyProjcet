# Solicitar ao usuário que insira três números distintos...

x = float(input("Digite o primeiro número (X): "))
y = float(input("Digite o segundo número (Y): "))
z = float(input("Digite o terceiro número (Z): "))

# Verificar se os números estão em ordem crescente
if x < y < z:
    print("Os números estão em ordem crescente.")
# Verificar se os números estão em ordem decrescente
elif x > y > z:
    print("Os números estão em ordem decrescente.")
# Caso contrário, estão misturados
else:
    print("Eles estão misturados!")