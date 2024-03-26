def juntarPalavras(palavra1, palavra2):

    palavrasJuntas = []
    i = 0
    j = 0

    while i < len(palavra1) or j < len(palavra2):
        if i < len(palavra1):
            palavrasJuntas += palavra1[i]
            i += 1
        if j < len(palavra2):
            palavrasJuntas += palavra2[j]
            j += 1

    return palavrasJuntas


palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

resultado = juntarPalavras(palavra1, palavra2)
print(resultado)
