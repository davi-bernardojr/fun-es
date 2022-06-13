def e_Primo(num):
    count = 0
    for x in range(1, num+1):
        if num % x == 0:            
            count += 1
    if count == 2:
        return True
    else:
        return False

def mostar_primo(aux):
    if e_Primo(aux) == True:
        print(f"O numero {aux} é primo")
    else:
        print(f"O numero {aux} não é primo")

numero = int(input("Informe um numero para verificar se o mesmo é primo ou não."))

mostar_primo(numero)
