# Demosntração de acesso a listas

print("Vou montar a marmita com 5 alimentos.")
MARMITA = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação.")

RESPOSTA= input("Você quer monstar uma marmita diferente (S/N)?")
if RESPOSTA == "S":
    for x in range (0,5):
        print(f"Digite o {x+1}o. item do cardápio:")
        MARMITA [x] = input ()
    print("A mamita montada foi:", MARMITA)    
    print("Os três primeiros itens foram:", MARMITA[0:3])
    print("O último item da marmita foi:", MARMITA[-1])
else:
    print("Ok! Você decide.")    
