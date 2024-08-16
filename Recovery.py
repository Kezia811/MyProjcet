    # Coletando os dados do usuário
NOME = input("Digite o seu nome: ")
SEXO = input("Digite o seu sexo (M para masculino, F para feminino, ou outro para não especificar): ")
IDADE = input("Digite a sua idade: ")
ENDEREÇO = input("Digite o seu endereço: ")

    # Mensagem personalizada com base no gênero
if SEXO () == 'M':
        MENSAGEM = "Bem-vindo, Sr. "
elif SEXO () == 'M':
        MENSAGEM = "Bem-vinda, Sra. "
else:
        MENSAGEM = "As portas estão abertas. "

    # Exibindo todos os dados
print(f"{MENSAGEM}{NOME}")
print(f"Idade: {IDADE} anos")
print(f"Endereço: {ENDEREÇO}")
