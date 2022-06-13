def fatorial (num):
    n = 1
    for x in range(num):
        n *= (x+1)
    return n

num = int(input("Informe um numero para obter o fatorial do mesmo."))

print(f"O fatorial do numero {num} é {fatorial(num)}")
