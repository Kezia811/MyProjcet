# Demonstração do uso da condicional...
print("Digite o número referente ao dia da semana")
print("1. segunda-feira")
print("2. terça-feira")
print("3. quarta-feira")
print("4. quinta-feira")
print("5. sexta-feira")
print("6. sábado ou domingo")
ESTADO= int(input())

match ESTADO:
    case 1:
        print("Ir ao SENAC")
    case 2:
        print("Ir à UERJ" )
    case 3:  
        print("Ir ao SENAC")
    case 4:
        print("Ir à UERJ")
    case 5: 
        print("Ir ao SENAC")
    case 6:
        print("Folga")