def FahToCelsius(valor):
    return (valor - 32) * 5/9


def CelsiusToFah(valor):
    return (valor*9/5) + 32


opcao = input(
    "Digite qual conversão deseja: Celsius -> Fahrenheit (F) / Fahrenheit -> Celsius (C) ").upper()

if opcao == 'F':
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = CelsiusToFah(celsius)
    print("A temperatura em Fahrenheit é:", resultado)

elif opcao == 'C':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = FahToCelsius(fahrenheit)
    print("A temperatura em Fahrenheit é:", resultado)

else:
    print("Opção inválida.")
