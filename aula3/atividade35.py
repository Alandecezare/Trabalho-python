def inverter_digitos(numero):
    numero_str = str(numero)

    numero_invertido = int(numero_str[::-1])

    return numero_invertido

def main():
    numero = int(input("Digite um número inteiro positivo de três dígitos (de 100 a 999): "))

    if 100 <= numero <= 999:
        numero_invertido = inverter_digitos(numero)

        print("O número formado pelos dígitos invertidos é:", numero_invertido)
    else:
        print("O número digitado não está dentro do intervalo de três dígitos (de 100 a 999).")

if __name__ == "__main__":
    main()