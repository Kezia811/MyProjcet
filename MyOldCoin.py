# Demonstração do uso da condicional...
print("Digite o número referente ao estado da moeda")
print("1. Flor de cunho")
print("2. Soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
ESTADO= int(input())

match ESTADO:
case 1:
print("Perfeita! Vou pagar R$ 1.000.000,00!")
case 2:
print("Quase perfeita! Ofereço R$ 250.000,00!" )
case 3:
print("Que ótimo! Posso dar uns 100.000,00!")
case 4:
print("Que bom aceiraria R$ 30.000,00?")
case 5: 
print("Desculpe, não aceito neste estado")
case _:
print("Opção não reconhecida")
