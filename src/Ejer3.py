def Reemplazar(lista,spoilers):
    for i in range(len(lista)):
        if lista[i].lower() in spoilers:
            lista[i] = "*"*len(lista[i])
    print(lista)