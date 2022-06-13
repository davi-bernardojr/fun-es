maiusculo = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
minusculo = "abcdefghijklmnopqrtuvwxyz"

def compara_Letra(texto, letras):
    soma = 0
    for x in texto:
        for y in letras:
            if x == y:
                soma += 1
    return soma

def exibe_Resultado(mais, minus):
    print(f"O numero de letras maiusculas é {mais}")
    print(f"O numero de letras minusculas é {minus}")

texto = input("Digite um texto")

exibe_Resultado(compara_Letra(texto, maiusculo), compara_Letra(texto, minusculo))



