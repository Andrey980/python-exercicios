def contador_vogais(palavra):
    vogais = 0
    conso = 0

    for letra in palavra:
        if letra in "aeiou":
            vogais += 1

        else:
            conso += 1

    return conso, vogais


valor = input("Digite uma palavra: ")

print("Conso e Vogais: ", contador_vogais(valor))
