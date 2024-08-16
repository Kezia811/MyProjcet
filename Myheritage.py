# Demosntração de OOP em Phyton

class CLIENTE:
    def __init__(self, TITULAR, CONTA, SALDO):
        self.TITULAR = TITULAR
        self.CONTA = CONTA
        self.SALDO = SALDO

class CLIENTE_FÍSICO(CLIENTE):
    def APRESENTAR(self):
        print("Olá! Eu sou:", self.TITULAR)
        print("Minha conta é:", self.CONTA)
        print("Eu quero saber o meu saldo.")
        return

    # Para criar uma estância baseada na classe CLIENTE
FULANO = CLIENTE_FÍSICO("João, 423.050.025-21", 25000,00)  

    # Executando o método da instância criada 
FULANO.APRESENTAR()

    #Acessando os atributos das instâncias criadas
print("De fato você realmente é:", FULANO.TITULAR) 
print("No momento a sua conta possui R$", FULANO.SALDO)