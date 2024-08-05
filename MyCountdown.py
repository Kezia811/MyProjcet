# Demosntração de contagem regressiva
def contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
    print("Feliz Ano Novo!")

if __name__ == "__main__":
    contagem_regressiva