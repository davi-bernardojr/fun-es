
def mostrar_soma(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma
    
lista = [5, 9, 1, 7, 3, 11, 1]

print(f'A soma total é {mostrar_soma(lista)}')