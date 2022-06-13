def testar_perfeito(num):
    if (num % 2) != 0:
        print(f"O numero {num} não é perfeito")
        return 
    meio = int(num / 2)    
    aux = []
    soma = 0
    for x in range(1, meio+1):
        if (num % x) == 0:
            aux.append(x)
    for y in aux:
        soma += y    
    if (soma == num):
        print(f"O numero {num} é perfeito")
    else:
        print(f"O numero {num} não é perfeito")
    
numero = int(input("Informe um numero para verificar se é ou não perfeito."))

testar_perfeito(numero)