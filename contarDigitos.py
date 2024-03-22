def contar_digitos(numero):
    numero_str = str(numero)
    contador = 0

    for digitos in numero_str:
        contador += 1

    return contador


numero = int(input("Digite um número inteiro: "))

quantidade_digitos = contar_digitos(numero)

print("O número de dígitos em", numero, "é:", quantidade_digitos)
