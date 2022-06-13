
def mostrar_multi(lista):
    for index, num in enumerate(lista):
        lista[index] = num * 2
    
lista = [5, 9, 1, 7, 3, 11, 1]

print(f'A lista é {lista}')

mostrar_multi(lista)

print(f'A lista multiplicada é {lista}')