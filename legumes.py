def legumes(lista):
    lista_invertida = lista[::-1]
    print('{', end='')
    for i in range (0, len(lista_invertida)):
        print(' %s' % (lista_invertida[i]), end = ": {")
    for i in range (0, len(lista_invertida)+1):
        print('}', end=' ')

if __name__ == "__main__":
    lista1 = ['batatas', 'cenouras', 'tomates', 'favas', 'pepinos', 'cebolas','beterrabas','alhos','couve']
    print(*lista1, sep=", ")
    legumes(lista1)