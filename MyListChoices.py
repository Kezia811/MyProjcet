# Demontração de funções em listas 
print("Eis, os meus maiores sonhos.")
SONHOS = ["1. Me divertir na Disney.",
          "2. Me banhar na praia de Sepetiba.",
          "3. Tirar férias em Paris.",
          "4. Fazer compras no West Shopping.",
          "5. Ver as pirâmides do Egito."]
for x in SONHOS:
    print(x)

print("Ops, não quero Sepetiba.")    
del(SONHOS[1])
print("E nem West Shopping.")
del(SONHOS [3])

print("Conferindo os sonhos.")
for x in SONHOS:
    print(x)