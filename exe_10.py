def triangulo(total_Linhas):
    content = []

    for count_1 in range(1, total_Linhas+1):
        content.append([])
        
    for count_1 in range(len(content)):
        for count_2 in range(count_1+1):
            content[count_1].append([])

    #se linha tiver 1 ou 2 posições preenche com 1 senão executa o algoritmo

    for count_1 in range(len(content)):
        for count_2 in range(count_1+1):
            if (count_2 == 0) or (count_2 == (count_1)):
                content[count_1][count_2] = 1
            else:
                content[count_1][count_2] = content[count_1-1][count_2-1] + content[count_1-1][count_2]

    for count_1 in range(len(content)):
        print(f"Linha {count_1+1} - {content[count_1]}")

triangulo(int(input("Informe o numero de linhas do triangulo.")))