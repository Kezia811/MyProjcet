# Revisão geral dos algorítimos & Lógica de Programação
print("Digite o seu nome")
NOME = input

IDADE = input("Digite a idade:")
ALTURA = input("Digite a altura:")

print(f"Meu nome é {NOME}")
print(f"Minha idade é {IDADE}")
print(f"Minha altura é {ALTURA}")

print(type(NOME))
print(type(IDADE))
print(type(ALTURA))

print("Qual será a minha idade em 2036?")
TEMPO = 2036 - 2024
IDADE =  IDADE + TEMPO
ALTURA = ALTURA / 2
print("A minha idade em 2036 será:", IDADE)

if IDADE < 18:
    print("Você é menor de idade.")
elif IDADE >= 18 and IDADE < 65:
    print("Você é maior de idade.")    
elif IDADE >= 65:
    print("Você já pode se aposentar.")
else
    print("Nada mais a fazer.")    
