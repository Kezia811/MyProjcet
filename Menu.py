# Demontração de café da manhã
print("Eis, as opções.")
CARDÁPIO = ["1. Pão com manteiga.",
          "2. Pão com ovo.",
          "3. Pão com queijo.",
          "4. Café puro.",
          "5. Café com leite."]
for x in CARDÁPIO:
    print(x)

print("Não gosto.")    
del(CARDÁPIO [1])
print("Eu quero.")
del(CARDÁPIO [3])

print("Conferindo os cardápios.")
for x in CARDÁPIO:
    print(x)