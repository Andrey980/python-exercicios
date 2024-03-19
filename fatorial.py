def calcFatorial(valor):
    valor_fatorial = 1

    for i in range(1, valor + 1):
        valor_fatorial = valor_fatorial * i

    return valor_fatorial


fatorial = int(input("Digite um número para calcular o fatorial: "))


if isinstance(fatorial, int) and fatorial >= 0:
    resultado = calcFatorial(fatorial)
    print("O fatorial do número ", fatorial, " é: ", resultado)
else:
    print("Digite um número válido!")
