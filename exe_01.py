
def mostrar_maior(lista):
    maior = 0
    for num in lista:
        if (num > maior):
            maior = num
    return maior
    
lista = [5, 9, 1, 7, 3, 11]

print(f'O maior numero é {mostrar_maior(lista)}')