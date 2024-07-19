# Posição dentro de campo
POSIÇÃO =input("Digite a posição que você joga: ")

if POSIÇÃO == "goleiro" or POSIÇÃO == "zagueiro" or POSIÇÃO == "lateral":
    print("Defesa")
elif POSIÇÃO == "volante" or POSIÇÃO == "meia":
    print("Meio-campo")
elif POSIÇÃO == "ponta" or POSIÇÃO == "atacante" or POSIÇÃO == "centroavante":
    print("Ataque")
else:
    print("Teimoso")