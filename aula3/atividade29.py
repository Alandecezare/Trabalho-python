dt = int(input("Digite o número de dias trabalhados: "))
sb = dt * 30
dp = sb * 0.11
dir = sb * 0.08
sl = sb - dp - dir

print(f"O salário a ser pago deve ser de {sl} ")