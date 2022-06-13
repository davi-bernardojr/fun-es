comand = 'n = 1\nfor x in range(1, 10):\n    n *= x\nprint(n)'

def executa_Comando():
    print(f"O codigo executado é o fatorial de 10 ")
    exec(comand)
    
executa_Comando()