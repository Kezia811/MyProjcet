# Demonstração da escalação 
def mostrar_escalacao(JOGADORES):
    print("Escalação atual:")
    for NÚMERO, NOME in JOGADORES.itens():
        print(f"Camisa {NÚMERO}: {NOME}")

def receber_escalacao():
    JOGADORES = {}
    print("Digite a escalação dos 11 jogadores titulares:")
    for _ in range(11):
        NOME = input("Nome do jogador: ")
        NÚMERO = input(f"Número da camisa de {NOME}: ")
        JOGADORES[NÚMERO] = NOME
    return JOGADORES

def realizar_substituicoes(JOGADORES):
    substituicoes = 3
    while substituicoes > 0:
        substituir = input(f"\nDeseja realizar uma substituição? (sim/não): ").lower()
        if substituir == "não":
            break
        elif substituir == "sim":
            numero_saida = input("Número da camisa do jogador a ser substituído: ")
            if numero_saida in JOGADORES:
                nome_saida = JOGADORES.pop(numero_saida)
                print(f"{nome_saida} (Camisa {numero_saida}) saiu.")
                nome_entrada = input("Nome do jogador que vai entrar: ")
                numero_entrada = input(f"Número da camisa de {nome_entrada}: ")
                JOGADORES[numero_entrada] = nome_entrada
                print(f"{nome_entrada} (Camisa {numero_entrada}) entrou.")
                substituicoes -= 1
            else:
                print("Jogador não encontrado na escalação.")
        else:
            print("Opção inválida.")
    return JOGADORES

def main():
    JOGADORES = receber_escalacao()
    mostrar_escalacao(JOGADORES)

    print("\nIntervalo do jogo.")
    JOGADORES = realizar_substituicoes(JOGADORES)
    mostrar_escalacao(JOGADORES)

if __name__ == "__main__":
    main()