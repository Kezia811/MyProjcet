# Programa para converter temperaturas...
print("Converter de Celsius para Kelvin e Fahrenheit...")
CELSIUS= int(input("Digite a temperatura:"))
KELVIN= CELSIUS + 273           
FAHRENHEIT= (9/5 + CELSIUS) - 32
print(f"A temperaturaem Kelvin será {KELVIN}.")
print(f"A temperaturaem Fahrenheint será {FAHRENHEIT}.")

#Seria possível utilizar as estruturas condicionais if/elif/else ou match/case, 
# para personalizar este programa, de forma que ele ofereça as três conversões?
# Por exemplo, ele poderia perguntar ao usuário qual a unidade de medidae qual
# valor de temperatura ele quer converter a partir daí , realizar os cálculos 
#necessários...
