def contar_digitos(numero):
    numero_str = str(numero)

    return len(numero_str)


numero = int(input("Digite um número inteiro: "))

quantidade_digitos = contar_digitos(numero)

print("O número de dígitos em", numero, "é:", quantidade_digitos)
