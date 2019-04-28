quantidade = 0
cont = False
with open("teste.java") as arquivo:
    for linha in arquivo:
        if cont == False:
            if '//' in linha:
                quantidade = quantidade + 1
            elif '/*' in linha and '*/' in linha:
                quantidade = quantidade + 1
            elif '/*' in linha:
                quantidade = quantidade + 1
                cont = True
        else:
            if '*/' in linha:
                quantidade = quantidade + 1
                cont = False
            else:
                quantidade = quantidade + 1
print(quantidade)