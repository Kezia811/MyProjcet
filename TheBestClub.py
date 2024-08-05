# Demosntração do melhor Clube de Futebol
melhor_clube = "Vasco"  
while True:
        resposta = input("Qual é o melhor clube de futebol do Brasil? ").strip()
        if resposta.lower() == melhor_clube.lower():
            print("Parabéns! Você acertou.")
            break
        else:
            print("Resposta incorreta. Tente novamente.")

if __name__ == "__main__":