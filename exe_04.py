def reverse_str(texto):
    txt = list(reversed(texto))
    ret_txt = ""
    for x in txt:
        ret_txt += x
    return ret_txt
    
texto = input('Digite um texto.')

print(f"O texto normal é {texto}")

print(f"O texto reverso é {reverse_str(texto)}")