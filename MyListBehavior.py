# Demosntração do comportamento das listas
print("Vou almoçar num restaurante a quilo.")

ORIGINAL = ["arroz", "Feijão", "batata", "alface", "frango"]
print("Eis, a minha comida:",  ORIGINAL)
DERIVADA = ORIGINAL
print("Meu amigo irá comer também.")

print("Vou altrar as opções sem ele ver.")
ORIGINAL.remove("arroz")
ORIGINAL.remove("feijão")
ORIGINAL.remove("alface")
ORIGINAL.remove("picanha")
ORIGINAL.remove("linguiça")

print("Amigo, me mostra o que você vai comer?")
print("Claro! Dá uma conferida", DERIVADA)
