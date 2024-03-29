def main():
    numero = int(input("Digite um número inteiro de 4 dígitos (de 1000 a 9999): "))

    if 1000 <= numero <= 9999:

        milhar = numero // 1000
        print("Milhar:", milhar)
        numero %= 1000
        centena = numero // 100
        print("Centena:", centena)
        numero %= 100
        dezena = numero // 10
        print("Dezena:", dezena)
        unidade = numero % 10
        print("Unidade:", unidade)
    else:
        print("O número digitado não está dentro do intervalo de 4 dígitos (de 1000 a 9999).")

if __name__ == "__main__":
    main()