def verificaPrimo(valor):

    if valor <= 1:
        return False

    elif valor <= 3:
        return True

    elif valor == 5:
        return True

    elif valor % 2 == 0 or valor % 3 == 0 or valor % 5 == 0:
        return False

    else:
        return True


num_primo = int(input("Digite um número inteiro positivo: "))

if isinstance(num_primo, int):
    resultado = verificaPrimo(num_primo)
    if resultado == True:
        print("O número é primo!")
    else:
        print("Não é primo!")

else:
    print("Digite um número válido!")
