# Este é um comentário!

LOCAL= input("Qual foi o local que você viajou")
match LOCAL:
    case "Disney": 
        print("Local excelente para levar as crianças!")
    case "Paris":
        print("Lugar perfeito para passeios românticos")   
    case _:
        print("Não conheço este lugar.")    