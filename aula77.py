def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Bem-vindo ao Conversor de Temperatura!")

    print("Escolha a unidade de temperatura de origem:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    escolha = int(input("Digite o número correspondente à sua escolha: "))

    temperatura = float(input("Digite a temperatura: "))

    if escolha == 1:
        print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(temperatura))
        print("Temperatura em Kelvin:", celsius_para_kelvin(temperatura))
    elif escolha == 2:
        print("Temperatura em Celsius:", fahrenheit_para_celsius(temperatura))
        print("Temperatura em Kelvin:", fahrenheit_para_kelvin(temperatura))
    elif escolha == 3:
        print("Temperatura em Celsius:", kelvin_para_celsius(temperatura))
        print("Temperatura em Fahrenheit:", kelvin_para_fahrenheit(temperatura))
    else:
        print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
