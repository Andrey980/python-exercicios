def calcular_media(lista):
    return sum(lista)/len(lista)


numeros = [float(x) for x in input(
    "Digite os números separados por vírgula: ").split(',')]
media = calcular_media(numeros)
print("A média dos números é:", media)
